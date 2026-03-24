<div align="center">

# 🤖 Peaky Setup Bot

**A simple, secure, and beginner-friendly Telegram bot to generate all the credentials you need for deploying Telegram bots.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0.106-green)](https://pyrogram.org/)
[![Telethon](https://img.shields.io/badge/Telethon-1.36.0-blue)](https://github.com/LonamiWebs/Telethon)
[![Channel](https://img.shields.io/badge/Telegram-eSportLeaker-26A5E4?logo=telegram)](https://t.me/eSportLeaker)

**Developer:** Satyam Xd

</div>

---

## 📖 Description

**Peaky Setup Bot** is an all-in-one assistant for setting up Telegram bots. It helps users:

- 🔑 **Generate a Pyrogram String Session** — step-by-step OTP flow with 2FA support
- 📘 **Get API ID & API HASH** — guided walkthrough for `my.telegram.org`
- 🤖 **Create a Bot Token** — guided walkthrough using `@BotFather`

No credentials are stored. All sensitive data is cleared immediately after use.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 String Session Generator | Guided OTP flow using Telethon |
| 📘 API ID & HASH Guide | Step-by-step instructions for `my.telegram.org` |
| 🤖 Bot Token Guide | Step-by-step instructions via `@BotFather` |
| 🔒 Secure | No data stored permanently; sensitive messages auto-deleted |
| 📱 Inline UI | Clean inline button navigation |
| ❌ Cancel anytime | `/cancel` to abort and clear data at any time |

---

## ⚙️ Commands

| Command | Description |
|---|---|
| `/start` | Show the main menu |
| `/help` | Show help information |
| `/cancel` | Cancel current operation and clear data |

---

## 🔧 Configuration

Create a `.env` file or export the following environment variables before running:

```env
BOT_TOKEN=your_bot_token_here

# Optional — defaults to Telegram's public test credentials.
# Set your own from https://my.telegram.org for better reliability.
API_ID=12345678
API_HASH=your_api_hash_here
```

Get your bot token from [@BotFather](https://t.me/BotFather).

---

## 🚀 Deployment

### 🐧 Ubuntu / VPS

```bash
# 1. Update system and install dependencies
sudo apt update && sudo apt install -y python3 python3-pip git

# 2. Clone the repository
git clone https://github.com/SatyamXd-Codex/PeakyHealperBot.git
cd PeakyHealperBot

# 3. Install Python dependencies
pip3 install -r requirements.txt

# 4. Set your bot token
export BOT_TOKEN="your_bot_token_here"

# 5. Run the bot
python3 main.py
```

### 📱 Termux (Android)

```bash
# 1. Install required packages
pkg install python git

# 2. Clone the repository
git clone https://github.com/SatyamXd-Codex/PeakyHealperBot.git
cd PeakyHealperBot

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set your bot token
export BOT_TOKEN="your_bot_token_here"

# 5. Run the bot
python main.py
```

### 🖥️ Windows

```powershell
# 1. Install Python 3.10+ from https://python.org

# 2. Clone the repository
git clone https://github.com/SatyamXd-Codex/PeakyHealperBot.git
cd PeakyHealperBot

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set your bot token
set BOT_TOKEN=your_bot_token_here

# 5. Run the bot
python main.py
```

---

## 📁 Project Structure

```
PeakyHealperBot/
├── bot/
│   ├── __init__.py
│   └── handlers/
│       ├── __init__.py
│       ├── start.py       # /start command & main menu
│       ├── help.py        # /help command
│       ├── cancel.py      # /cancel command
│       ├── session.py     # String session generation (FSM)
│       └── guides.py      # API & Bot Token guide callbacks
├── config/
│   ├── __init__.py
│   └── config.py          # Configuration (BOT_TOKEN)
├── helpers/
│   ├── __init__.py
│   ├── keyboards.py       # Inline keyboard builders
│   └── messages.py        # All message text constants
├── main.py                # Entry point
├── requirements.txt
└── README.md
```

---

## 🔒 Security

- **No data is stored** — all user credentials and sessions exist only in memory during the generation flow
- **Sensitive messages are auto-deleted** — phone numbers, OTP codes, and 2FA passwords are deleted immediately after reading
- **Telethon client is disconnected** after session generation or cancellation

---

## 📢 Links

[![Join Channel](https://img.shields.io/badge/Telegram-Join%20Channel-26A5E4?logo=telegram&style=for-the-badge)](https://t.me/eSportLeaker)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">Made with ❤️ by <b>Satyam Xd</b></div>