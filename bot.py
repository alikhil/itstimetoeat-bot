import telegram
from telegram.ext import CommandHandler, Updater,  MessageHandler, Filters

import logging

from config import *
from predictor import get_prediction

bot = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(context, update):
    context.send_message(
        chat_id=update.message.chat_id, 
        text="""
Hey! It's time to eat! 🌭 
Use /help to get list of available commands.
"""
    )

def help(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="""
Avaiable commands 🍔:

/i_am_hungry - show queue image and prediction 🍗
/itstimetoeat - show labeled queue image and prediction 🍪
        """
    )

def echo(context, update):
    print('kek', update)
    context.send_message(chat_id=update.message.chat_id, text=update.message.text)

def simple_demo(bot, update):
    prediction = get_prediction(labeled=False)
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=prediction['picture'],
        caption=prediction['message'])

def labeled_demo(bot, update):
    prediction = get_prediction(labeled=True)
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=prediction['picture'],
        caption=prediction['message'])


help_handler = CommandHandler('help', help)
start_handler = CommandHandler('start', start)
simple_demo_handler = CommandHandler('i_am_hungry', simple_demo)
labeled_demo_handler = CommandHandler('itstimetoeat', labeled_demo)
echo_handler = MessageHandler(Filters.text, echo)

bot.dispatcher.add_handler(start_handler)
bot.dispatcher.add_handler(echo_handler)
bot.dispatcher.add_handler(help_handler)
bot.dispatcher.add_handler(simple_demo_handler)
bot.dispatcher.add_handler(labeled_demo_handler)

bot.start_polling(poll_interval=1)