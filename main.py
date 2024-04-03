import threading

from bot.bot import telegram_bot
from services.statistics.statistics import statistics

if __name__ == '__main__':
    print(threading.active_count())
    
    telegram_bot_thread = threading.Thread(target=telegram_bot, args=())
    telegram_bot_thread.start()
    
    statistics_thread = threading.Thread(target=statistics, args=())
    statistics_thread.start()
    
    print(threading.active_count())