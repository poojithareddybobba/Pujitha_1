# 🎤 Voice_Assistant 

A simple Python-based Voice Assistant that listens to voice commands and responds using text-to-speech. This project demonstrates the basics of speech recognition and voice interaction using Python.

## 📌 Objective

Build a beginner-friendly voice assistant that can:

* Capture voice input using a microphone
* Respond to basic voice commands
* Convert text responses into speech
* Handle speech recognition errors gracefully

## ✨ Features

* 🎙️ Capture voice input using **SpeechRecognition**
* 🔊 Respond using **pyttsx3** text-to-speech
* 👋 Greet the user
* 🙋 Introduce itself
* 😂 Tell a joke
* 👂 Listen continuously until the user says **"Goodbye"**
* ⚠️ Handle speech recognition and network errors gracefully

## 🛠️ Technologies Used

* Python 3.14.6
* SpeechRecognition
* pyttsx3
* PyAudio

## 📂 Project Structure

```
├──venv/
├── voice_assistant.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/poojithareddybobba/Voice_Assisstent.git
```

### 2. Navigate to the beginner folder

```bash
cd Voice_Assisstent/beginner
```

### 3. (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python voice_assistant_beginner.py
```

## 🎤 Supported Voice Commands

* **Hello**
* **What's your name?**
* **Tell me a joke**
* **Goodbye**

## 📦 Requirements

```
SpeechRecognition
pyttsx3
PyAudio
```

## ⚠️ Notes

* Ensure your microphone is connected and working.
* An internet connection is required for Google's speech recognition service.
* If your voice isn't recognized, the assistant will ask you to repeat.

## 📸 Sample Output

```text
Assistant: Hello! How can I assist you?

You: Hello

Assistant: Hello! How can I assist you?

You: What's your name?

Assistant: My name is Voice Assistant.

You: Tell me a joke.

Assistant: Why don't scientists trust atoms? Because they make up everything!

You: Goodbye

Assistant: Goodbye!
```

## 👩‍💻 Author

**Poojitha Reddy Bobba**

GitHub: https://github.com/poojithareddybobba

## 📄 License

This project was created for learning purposes as part of the **Oasis Infobyte Internship Program**.
