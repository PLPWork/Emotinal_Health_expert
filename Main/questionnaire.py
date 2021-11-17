#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
import logging
import sqlite3
from tabulate import tabulate
import telegram_bot
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from telegram.utils.request import Request

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
import logging
from _model import *

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, user
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TENSE, ENJOY, LOST, CLINIC ,BEFORE,END,NEW = range(7)

s1="Let me help you figure out what''s going on, would you like share a little bit more about you?"
base_que="Over the last 2 weeks, how often have you been bothered by any of the following problems?"
options=["Not at all", "Several days", "More than half the days", "all the days"]

user_que=[
	 MultiItems("Little interest or pleasure in doing things", options)    
	,MultiItems("Feeling down, depressed, or hopeless", options)    
	,MultiItems("Feeling tired or having little energy", options)    
	,MultiItems("Trouble falling or staying asleep, or sleeping too much", options)    
	,MultiItems("Feeling bad about yourself - or that you are a failure or have let yourself or your family down", options)    
	,MultiItems("Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", options)    
	,MultiItems("Thoughts that you would be better off dead or of hurting yourself in some way", options)    
	,MultiItems("Feeling nervous, anxious, or on edge", options)    
	,MultiItems("Not being able to stop or control worrying", options)    
	,MultiItems("Worrying too much about different things", options)    
	,MultiItems("Trouble relaxing", options)    
	,MultiItems("Becoming easily annoyed or irritable", options)    
	,MultiItems("Feeling afraid as if something awful might happen", options)    
	,MultiItems("How difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?", options)    
	,MultiItems("I have felt calm and relaxed", options)    
	,MultiItems("I have felt active and vigorous", options)    
	,MultiItems("I woke up feeling fresh and rested", options)    
	,MultiItems("My daily life has been filled with things that interest me", options)    
	,MultiItems("What is your age?", ["under 18","under 30", "under 50", "above 50"])    
	,MultiItems("May I have your gender?", ["female","male","not disclosing"])    
	,MultiItems("Do you have any substance abuse?",["yes","no"])    
	,MultiItems("Do you have any chronic health condition?", ["yes","no"])    
	,MultiItems("Do you have any financial trouble in the recent times?", ["yes","no"])    
	,MultiItems("Are you going through separation or lost someone close?", ["yes","no"])    ]

def start(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(chat_id=update.message.chat_id, text=base_que)
    button = user_que[0]
    button=MultiItems("Do you have any financial trouble in the recent times?",options)  
    add_suggested_actions(update, context, button)

    return TENSE

def add_suggested_actions(update, context, response):
    options = []

    for item in response.items:
        options.append(InlineKeyboardButton(item, callback_data=item))

    reply_markup = InlineKeyboardMarkup([options])

    # update.message.reply_text(response.message, reply_markup=reply_markup)
    context.bot.send_message(chat_id=get_chat_id(update, context), text=response.message, reply_markup=reply_markup)

def get_chat_id(update, context):
    chat_id = -1

    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id
    elif update.poll is not None:
        chat_id = context.bot_data[update.poll.id]

    return chat_id


def Tense(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Answer submitted %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'May I have your gender ? "Female","Male","Not disclosing" ',
        reply_markup=ReplyKeyboardRemove(),
    )

    return ENJOY


def enjoy(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    logger.info("Answer submitted %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Do you have any substance abuse "yes" "no"',
        reply_markup=ReplyKeyboardRemove()
    )

    return LOST


def skip_photo(update: Update, context: CallbackContext) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text(
        'I bet you look great! Now, send me your location please, or send /skip.'
    )

    return LOCATION


def lost(update: Update, context: CallbackContext) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Answer submitted by %s: %f / %f", user.first_name, user.first_name, update.message.text
    )
    update.message.reply_text(
        'Do you have any chronic health condition "yes","no"'
    )

    return CLINIC


def skip_before(update: Update, context: CallbackContext) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User skipped", user.first_name)
    update.message.reply_text(
        'Ok got it.'
    )

    return END

def before(update: Update, context: CallbackContext) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'Okay we are almost done with the questionnaire ,do you want to skip or cancel'
    )

    return END

def NEW(update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Answer given by %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Are you going through seperation or lost someone,"yes","no"')

    return END


def clinic(update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Answer given by %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Did you have any financial trouble in recent times,"yes","no"')

    return NEW

def END(update: Update, context: CallbackContext) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Answer given by %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Okay it was nice talking to you ,we found that you are a litlle bit depressed ,no need to worry you can talk to use')

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2136371314:AAHP7Jsx1hIqtdqIOZ6UhFT90Eabu5eDTEU")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TENSE: [MessageHandler(Filters.text, Tense)],
            ENJOY: [MessageHandler(Filters.text, enjoy)],
            LOST: [
                MessageHandler(Filters.text, lost),
            ],
            NEW: [MessageHandler(Filters.text, NEW)],
            CLINIC: [MessageHandler(Filters.text,clinic)],
            BEFORE: [MessageHandler(Filters.text,before),CommandHandler('skip', skip_before)],
            END: [MessageHandler(Filters.text,END)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()