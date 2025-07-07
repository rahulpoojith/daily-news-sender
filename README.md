# 📰 Daily News Sender via Email

This Python project sends daily personalized news articles to users based on their selected interest. News is fetched using the [NewsAPI](https://newsapi.org/) and delivered via email using the `yagmail` library.

---

## 🚀 Features

- Sends automated emails with news headlines and links.
- Customizable by user interest (e.g., technology, sports, NASA).
- Scheduled to send daily at a specific time.
- Reads recipient info and interests from an Excel file.
- Uses the `NewsFeed` class to interact with NewsAPI.

---

## 📁 Project Structure

```
daily-news-sender/
├── main.py              # Main script to send emails daily
├── news.py              # NewsFeed class to fetch headlines from NewsAPI
├── people.xlsx          # Excel sheet with user emails and interests
├── design.txt           # Notes or design documentation
├── .env                 # Environment variables (not committed)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---

## 🛠️ Setup Instructions

### 1. Install Required Packages

```bash
pip install yagmail pandas openpyxl requests python-dotenv
```

### 2. Set Up Gmail App Password

Gmail requires an **App Password** for secure programmatic access:

1. Go to: https://myaccount.google.com/apppasswords
2. Enable 2-Step Verification if not already enabled.
3. Generate a password for "Mail" on your device.
4. Copy and use this password in your `.env` file.

---

## 🔐 Environment Variable Setup

Create a `.env` file in your project directory:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
NEWS_API_KEY=your_newsapi_key
```

### Example usage in `main.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")
```

Add `.env` to `.gitignore` so secrets are never pushed:

```bash
echo ".env" >> .gitignore
```

---

## 📧 Email Sample

```
Subject: Your NASA news for 2025-07-07

Here is your news for 2025-07-07:

NASA launches new satellite  
https://example.com/article1

Astronomers discover new exoplanet  
https://example.com/article2
```

---

## ⏱️ Automating the Email (Schedule)

The script checks the current time and sends emails at a specific hour/minute:

```python
if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 51:
```

To make it persistent:
- Run it on a server
- Or schedule using `cron` (Linux/macOS) or Task Scheduler (Windows)

---

## 📜 License

MIT License. Free to use and modify.

---

## 🙋‍♀️ Contributions

Feel free to fork this repo and improve upon it — whether it's by:
- Adding HTML email formatting
- Logging delivery history
- Using advanced scheduling tools like APScheduler
