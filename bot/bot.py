def telegram_bot():

    import os
    import telebot

    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    print("[>] Configuring Telegram bot")

    @telegram_bot.message_handler(commands=['hello'])
    def send_hello(message):
        print("[!] 'hello' command 👋")
        telegram_bot.reply_to(message, "Howdy, how are you doing?")
        print("[>] Responded to 'hello' command")
                
    @telegram_bot.message_handler(commands=['daily'])
    def send_daily_statistics(message):
        print("[!] 'daily' command 📊")
        telegram_bot.reply_to(message, "WIP!")
        print("[>] Responded to 'daily' command")

    print("[>] Telegram bot is now online 🟢")
    telegram_bot.infinity_polling()