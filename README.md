# 🗣️ Speech Recognition Desktop App

This is a simple Speech-to-Text desktop application built using **Python**, **SpeechRecognition**, and **Tkinter**. The app allows users to speak into their microphone and transcribes their speech in real time.

## ✨ Features

- Live speech recognition using microphone
- Transcribes spoken words into text
- Clean and interactive GUI with Tkinter
- Option to save transcribed text
- Visual indicators for recording status

## 🛠 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Make sure to install **PyAudio** properly:
- On Windows: download the correct `.whl` file from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- On Linux: `sudo apt-get install portaudio19-dev && pip install pyaudio`

## 🚀 Run the App

```bash
python speech_recognizer.py
```

## 📂 Directory Structure

```
.
├── speech_recognizer.py      # Main application script
├── requirements.txt
├── README.md
└── .gitignore
```

## 📃 License

This project is licensed under the MIT License.

## 🤝 Contributing

Feel free to fork and contribute. Open an issue to discuss major changes.