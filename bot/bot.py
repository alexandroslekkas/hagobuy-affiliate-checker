import os
import telebot
from services.statistics.statistics import calculate_daily_stats

def telegram_bot(): 
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    print("[>] Configuring Telegram bot")

    @bot.message_handler(commands=['hello'])
    def send_hello(message):
        print("[!] 'hello' command 👋")
        bot.reply_to(message, "Howdy, how are you doing?")
        print("[>] Responded to 'hello' command")
                
    @bot.message_handler(commands=['daily'])
    def send_daily_statistics(message):
        print("[!] 'daily' command 📊")
        daily_stats = calculate_daily_stats()
        bot.reply_to(message, daily_stats)
        print("[>] Responded to 'daily' command")

    print("[>] Telegram bot is now online 🟢")
    bot.infinity_polling()