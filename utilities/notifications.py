import os
from telegram import Bot

# Function to send a notification through Telegram
async def send_notification(message):
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot_chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = Bot(token=bot_token)
    
    await bot.send_message(chat_id=bot_chat_id, text=message)