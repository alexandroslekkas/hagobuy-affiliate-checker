import telebot
import os

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_message(message):
    bot_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot.send_message(chat_id=bot_chat_id, text=message)