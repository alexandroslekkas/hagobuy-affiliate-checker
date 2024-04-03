

def telegram_bot(): 
    import os
    import telebot

    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    from services.statistics.statistics import calculate_daily_stats
    print("[>] Configuring Telegram bot")

    @telegram_bot.message_handler(commands=['hello'])
    def send_hello(message):
        print("[!] 'hello' command 👋")
        telegram_bot.reply_to(message, "Howdy, how are you doing?")
        print("[>] Responded to 'hello' command")
                
    @telegram_bot.message_handler(commands=['daily'])
    def send_daily_statistics(message):
        print("[!] 'daily' command 📊")
        daily_stats = calculate_daily_stats()
        telegram_bot.reply_to(message, daily_stats)
        print("[>] Responded to 'daily' command")

    print("[>] Telegram bot is now online 🟢")
    telegram_bot.infinity_polling()