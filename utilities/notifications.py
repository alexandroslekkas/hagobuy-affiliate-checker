import asyncio
import os
from telegram import Bot

# Function to send a notification through Telegram
async def send_notification(message):
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot_chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = Bot(token=bot_token)
    
    # Run the synchronous code in the event loop's executor
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, bot.send_message, bot_chat_id, message)