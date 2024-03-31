# 🌟 HagoBuy Affiliate Statistics Tracker 🌟

Automates logging into HagoBuy, navigating to the affiliate center, and extracting key statistics. Built with Selenium, it operates in headless mode for seamless automation.

## 🚀 Features

- 🗝️ Automated login to HagoBuy
- 📊 Navigation and extraction of affiliate statistics
- 🕶️ Runs in headless mode for background execution
- 🤖 Sends extracted statistics via Telegram bot

## 📋 Requirements

- Python 3.6+
- Selenium
- ChromeDriver

## ⚙️ Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://your-repo-link.git
cd hagobuy-affiliate-checker
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

## 🔧 Configuration

Create a `.env` file in the root directory with your credentials:

```plaintext
# HagoBuy Account Credentials
HAGOBUY_ACCOUNT_EMAIL=your-email@example.com
HAGOBUY_ACCOUNT_PASSWORD=your_password

# Telegram Bot for Notifications
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 🚀 Usage

Run the script with:

```bash
python main.py
```

The script logs into HagoBuy, navigates to the affiliate center, extracts statistics, and sends them via Telegram.

## 🤝 Contributing

Contributions are welcome!

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.