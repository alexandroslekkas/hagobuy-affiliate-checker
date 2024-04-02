import threading

from telegram_bot import telegram_bot
from loop import loop

if __name__ == '__main__':
    print(threading.active_count())
    telegram_bot_thread = threading.Thread(target=telegram_bot, args=())
    telegram_bot_thread.start()
    loop_thread = threading.Thread(target=loop, args=())
    loop_thread.start()