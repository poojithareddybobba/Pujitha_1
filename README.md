# 🎙️ Python Voice Assistant

A simple **Voice Assistant built using Python** that listens to voice commands, understands them, and responds using voice.

This project is beginner-friendly and demonstrates **Speech Recognition, Text-to-Speech, Date & Time, and Google Search** using Python.

---

## ✨ Features

- 🎤 Recognizes voice commands through the microphone
- 🔊 Responds using voice
- 👋 Responds to "Hello"
- 🕐 Tells the current time
- 📅 Tells today's date
- 🔎 Searches Google using voice commands
- ❌ Stops when you say "Exit" or "Stop"
- ⚠️ Handles speech recognition errors
- 🪟 Uses Windows SAPI for text-to-speech

---

## 🛠️ Technologies Used

- 🐍 **Python 3.13**
- 🎤 **SpeechRecognition** – Converts speech into text
- 🔊 **PyWin32** – Provides Windows text-to-speech using SAPI
- 🎙️ **PyAudio** – Captures microphone input
- 🕐 **datetime** – Gets the current date and time
- 🌐 **webbrowser** – Opens Google search results

---

## 📁 Project Structure

```text
PUJITHA_01/
│
├── .venv/
├── README.md
├── requirement.txt
└── voice_assisstent.py
---

⚙️ Requirements

Before running this project, make sure you have:

Python 3.13

Windows OS

Working microphone

Internet connection

VS Code (recommended)
---

📦 Installation

1. Clone the Repository

git clone https://github.com/poojithareddybobba/Pujitha_1.git

2. Navigate to the Project Folder

cd Pujitha_1

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

For Windows PowerShell:

.\.venv\Scripts\Activate.ps1

After activation, you should see:

(.venv) PS C:\...\Pujitha_1>

5. Install Required Packages

Since your file is named requirement.txt, use:

python -m pip install -r requirement.txt


---

📋 requirement.txt

Your requirement.txt file should contain:

SpeechRecognition
PyWin32
PyAudio

You can also install the packages manually:

python -m pip install SpeechRecognition
python -m pip install PyWin32
python -m pip install PyAudio


---

▶️ How to Run

Make sure your virtual environment is activated.

Run:

python voice_assisstent.py

The assistant will start with:

Assistant: Hello! I am your Voice Assistant.

Then speak a command through your microphone.


---

🗣️ Example Voice Commands

Voice Command	Action

Hello	Greets you
how are you
what's your name
What is the time	Tells the current time
What is the date	Tells today's date
Search Python tutorials	Searches Google
ok thank you or thanks
Exit	Closes the assistant
Stop	Closes the assistant


Example

You: Hello
Assistant: Hello! How can I help you?

You: What is the time?
Assistant: The current time is 07:30 PM

You: What is the date?
Assistant: Today's date is 10 August 2026

You: Search Python tutorials
Assistant: Searching Google for Python tutorials

You: Exit
Assistant: Goodbye!


---

🔄 How It Works

🎤 Microphone
              ↓
      Speech Recognition
              ↓
        Voice → Text
              ↓
      Process the Command
              ↓
        Perform Action
              ↓
       Windows SAPI
              ↓
       🔊 Voice Response


---


🚀 Future Improvements

Some features that can be added in the future:

🌦️ Weather information

🎵 Music playback

🌐 Open websites using voice

📂 Open applications and folders

⏰ Reminders and alarms

📧 Send emails using voice

📖 Wikipedia search

📰 News updates

🤖 More intelligent voice commands

🖥️ Graphical User Interface (GUI)

---

👩‍💻 Author

Poojitha Reddy Bobba

GitHub:
https://github.com/poojithareddybobba/Pujitha_1


---

⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

Thank you for checking out my Python Voice Assistant! 🎙️🐍

## 📄 License

This project was created for learning purposes as part of the **Oasis Infobyte Internship Program**.
