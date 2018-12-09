import random

import telebot
from apscheduler.schedulers.blocking import BlockingScheduler
import config


def greetings():
    try:
        bot = telebot.TeleBot(config.bot_api_token, threaded=False)
        bot.send_message(config.chat_id, "Бот запущен. Оповещение придет в {}:{}".format(config.n_hour,
                                                                                         config.n_minute))
    except Exception as ex:
        print(ex.args)


def main():
    foo = ['в пацанскую', 'во Фламинго']
    choice = random.choice(foo)

    try:
        bot = telebot.TeleBot(config.bot_api_token, threaded=False)
        bot.send_message(config.chat_id, "Сегодня вы идете жрать {}".format(choice))
    except Exception as ex:
        print(ex.args)


if __name__ == '__main__':
    greetings()
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'cron', day_of_week='mon-fri', hour=config.n_hour, minute=config.n_minute)
    scheduler.start()
