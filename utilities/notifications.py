from telegram import Bot
import os

async def send_notification(message):
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = Bot(token=bot_token)

    # If send_message is async, await it directly
    await bot.send_message(chat_id=bot_chat_id, text=message)
