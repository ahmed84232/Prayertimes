# 🕌 Prayer Times Notifier with Azan

A Python-based desktop application that fetches Islamic prayer times using your location and notifies you with both a Windows notification and the Azan sound at the correct time.

## 📦 Features

- Auto-fetches your IP and location.
- Gets accurate prayer times using the IslamicFinder API.
- Sends Windows notifications for each prayer.
- Plays the Azan (`Al-Azan.mp3`) when prayer time comes.

## 🖥️ Requirements

- Python 3.6+
- Internet connection

### 🧰 Python Dependencies

Install them with pip:

pip install requests plyer playsound

#### ▶️ How to Run
- Make sure main.py, config.txt, and Al-Azan.mp3 are in the same directory.
- Open a terminal or command prompt.
- Run the script: python main.py

The app will print your current time and today's prayer times, then stay running in the background to notify you.

