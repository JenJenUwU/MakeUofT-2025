import asyncio
import os
import serial
import time
from googletrans import Translator
from faster_whisper import WhisperModel
from gtts import gTTS

PORT = "COM3"  # Change this based on your system (e.g., "/dev/ttyUSB0" for Linux)
BAUD_RATE = 115200
FILE_NAME = "received_audio.wav"

# Open Serial connection
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

model = WhisperModel("small", "cpu", compute_type="float32")
google_translator = Translator()

def send_text_to_arduino(text):
    ser.write(text.encode())
    ser.write(b'\n')  # Send newline character to indicate end of message

# Modify the main function to send the transcribed text
async def main():
    # Wait for Arduino ready signal
    while True:
        response = ser.readline().decode().strip()
        if response == "READY":
            print("[INFO] Arduino is ready.")
            break

    print("[INFO] Waiting for new recordings...")
    while True:
        print(f"[SERIAL OUTPUT] {response}")  # Print serial port output
        response = ser.readline().decode().strip()
        if response == "SENDING":
            print("[INFO] Receiving new file...")

            # Delete the previous copy of the file if it exists
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)

            with open(FILE_NAME, "wb") as f:
                while True:
                    data = ser.read(64)  # Read in chunks
                    if b"DONE" in data:
                        f.write(data.replace(b"DONE", b""))  # Remove DONE signal
                        break
                    f.write(data)

            print(f"[INFO] File received and saved as {FILE_NAME}")

            # Transcription Process
            print("[INFO] Processing transcription...")
            segments, _ = model.transcribe(FILE_NAME, beam_size=5)
            transcription = " ".join(segment.text for segment in segments)
            translated_text = await google_translator.translate(transcription, dest="en")
            print(translated_text.text)

            print("[INFO] Transcription complete!")

            # Send transcribed text to Arduino
            send_text_to_arduino(translated_text.text)

            # Listen for the next recording
            print("[INFO] Waiting for new recordings...")

# Run the main function
asyncio.run(main())