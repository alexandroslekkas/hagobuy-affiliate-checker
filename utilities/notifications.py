import os
from telegram import Bot

# Function to send a notification through Telegram
async def send_notification(message):
    bot_token = os.environ['BOT_TOKEN']
    bot_chatID = '6675952317'
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=bot_chatID, text=message)