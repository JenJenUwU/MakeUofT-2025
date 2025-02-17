# Verba Link

Verba Link is a project that facilitates communication between an Arduino device and a Python application. The Arduino records audio, sends it to the Python application for transcription and translation, and then receives the translated text back to play it using a text-to-speech module.

## Features

- Record audio using an Arduino and save it to an SD card.
- Send recorded audio to a Python application via serial communication.
- Transcribe the audio using the Whisper model.
- Translate the transcribed text using Google Translate.
- Convert the translated text to speech using gTTS.
- Send the translated text back to the Arduino for playback.

## Requirements

### Hardware

- Arduino board
- SD card module
- Microphone
- Speaker
- Push button
- LED

### Software

- Python 3.8+
- Arduino IDE
- PySerial
- Googletrans
- gTTS
- ffmpeg
- faster-whisper

## Installation

### Arduino

1. Install the [TMRpcm](https://github.com/TMRh20/TMRpcm) library in the Arduino IDE.
2. Upload the `record.ino` sketch to your Arduino board.

### Python

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/verba-link.git
    cd verba-link
    ```

2. Install the required Python packages:
    ```sh
    pip install pyserial googletrans gtts faster-whisper
    ```

3. Ensure `ffmpeg` is installed and available in your system's PATH.

## Usage

1. Connect the Arduino to your computer via USB.
2. Run the Python script to start the transcription and translation process:
    ```sh
    python receive.py
    ```
3. Press the button on the Arduino to start recording audio.
4. The Arduino will send the recorded audio to the Python application for processing.
5. The Python application will transcribe, translate, and convert the text to speech.
6. The translated text will be sent back to the Arduino for playback.

## File Structure

- `record.ino`: Arduino sketch for recording and sending audio.
- `receive.py`: Python script for receiving audio, transcribing, translating, and sending text back to Arduino.
- `test.py`: Python script for converting audio formats using ffmpeg.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [TMRpcm](https://github.com/TMRh20/TMRpcm) library for audio recording and playback on Arduino.
- [faster-whisper](https://github.com/openai/whisper) for transcription.
- [Googletrans](https://github.com/ssut/py-googletrans) for translation.
- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech conversion.
- [ffmpeg](https://ffmpeg.org/) for audio format conversion.
