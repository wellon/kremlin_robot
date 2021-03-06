import random

import telebot
from apscheduler.schedulers.blocking import BlockingScheduler
from telebot import apihelper

import config

apihelper.proxy = {'https': config.socks}


def greetings():
    try:
        bot = telebot.TeleBot(config.bot_api_token, threaded=False)
        bot.send_message(config.chat_id, "Бот запущен. Оповещение придет в {}:{}".format(config.n_hour,
                                                                                         config.n_minute))
    except Exception as ex:
        print(ex.args)


def main():
    foo = config.choices
    choice = random.choice(foo)

    try:
        bot = telebot.TeleBot(config.bot_api_token, threaded=False)
        bot.send_message(config.chat_id, "Сегодня вы идете жратБ в {}".format(choice))
    except Exception as ex:
        print(ex.args)


if __name__ == '__main__':
    greetings()
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'cron', day_of_week='mon-fri', hour=int(config.n_hour), minute=int(config.n_minute))
    scheduler.start()
