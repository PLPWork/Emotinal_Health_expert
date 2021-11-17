from scipy.sparse import dia
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
import logging
import sqlite3
from tabulate import tabulate

import time
#import FAQlogic
#import tfidf_doc_search
#import bert_question
import faq_copy
import telegram_bot
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from telegram.utils.request import Request

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
import pandas as pd
import bert_question_copy
import time
import re
import pyfiglet
import logging
import logging.config
import os
import requests
import itertools

from _model import *


bot=telegram.Bot(token='2136371314:AAHP7Jsx1hIqtdqIOZ6UhFT90Eabu5eDTEU')
updater = Updater(token='2136371314:AAHP7Jsx1hIqtdqIOZ6UhFT90Eabu5eDTEU',use_context=True)

dialog_states=['greeting',"survey",'q_a_c','q_a_b','goodbye']
ss_index=[0]
dialog_state=['goodbye']

bert_kb=[0,1,2]
#bert_kb[0]=pd.read_csv("C:/Users/verma/Documents/GitHub/Sem4PLPPrj/Main_code/TelegramBot-PizzaOrderBot-master/Depression.txt",sep="\t")
bert_kb[0]="Sometimes it is scarier to journey into the unknown (in this case, happiness), than it is to stay in the known, and the oftentimes comfortable space of your depression. Human beings, for the most part, fear and stray away from change in general, especially a change that is so impactful--It isn’t abnormal. Anything that you are well-acquainted with can become comfortable, and that includes suffering. When you have been depressed for a long time, that can feel like the only natural state, so you miss it when it is gone, even if you know that it isn’t good for you.Indeed, depression can have a significant impact on both your health and your well-being PTSD can be diagnosed by your primary care provider or a mental health professional.Post-traumatic stress disorder (PTSD)is a trauma and stressor-related disorder that can develop after a traumatic or stressful event.Bipolar affective disorder typically consists of both manic and depressive episodes separated by periods of normal mood Manic episodes involve elevated mood and increased energy resulting in over-activity, pressure of speech and decreased need for sleep.--Self-harm is also commonly known as self-injurious behaviour (SIB),self-mutilation, non-suicidal,self-injury (NSSI), parasuicide,deliberate self-harm (DSH),self- abuse, and self-inflicted violence (Klonsky, 2011).As one would expect, having multiple terms for self-harm creates misunderstandingand confusion both in academic research and in clinical settings.COGNITIVE BEHAVIOUR THERAPY (CBT)is a psychological therapy that aims to address issues such as anxiety and depression, as well as a range of other mental health concerns. It helps someone become aware of inaccurate or negative thinking,so challenging situations can be seen more clearly and responded to more effectively.PROBLEM SOLVING THERAPY (PST)is a brief psychological intervention that focuses on identifying the specific problems that an individual is facing and generating alternative solutions to these problems.Individuals learn to clearly define a problem that they face, brainstorm multiple solutions, and decide on the best course of action"
    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#Function to start the bot,initiated on /start command
def start(update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Hi, I am you pal - how are u doing today?')
TI=1
def greeting_section(msg, update: Update, context: CallbackContext):
    #if(not dialog_state.endWith('greeting')):
    #    print("incorrect dialog state")
    #    return
    if(msg.endswith('depressed')):
        context.bot.send_message(chat_id=update.message.chat_id, text='I m sure you are going through a lot!')
        time.sleep(TI)
        context.bot.send_message(chat_id=update.message.chat_id, text='Do you need someone to talk with? I am here for you!')
    elif(msg.endswith('yes')):
        context.bot.send_message(chat_id=update.message.chat_id, text='Sometimes life doesnt treat you well but there is always a hope')
        time.sleep(TI)
        context.bot.send_message(chat_id=update.message.chat_id, text='Let me help you figure out what''s going on, would you like share a little bit more about you?')
    elif(msg.endswith('ok')):
        changeDialogState("survey")
        context.bot.send_message(chat_id=update.message.chat_id, text='Great! Let us dive a little deeper, You can always end by saying - "end survey"')
        time.sleep(TI)
        context.bot.send_message(chat_id=update.message.chat_id, text='These next questions are clinically validated to help us understand - How you’ve been feeling, and to track your progress in the weeks ahead.')
        time.sleep(TI)
    
        surveyQueAns(update,context, 0)

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

    #,MultiItems("What is your age?", ["under 18","under 30", "under 50", "above 50"])    
	#,MultiItems("May I have your gender?", ["female","male","not disclosing"])    
	#,MultiItems("Do you have any substance abuse?",["yes","no"])    
	#,MultiItems("Do you have any chronic health condition?", ["yes","no"])    
	#,MultiItems("Do you have any financial trouble in the recent times?", ["yes","no"])    
	#,MultiItems("Are you going through separation or lost someone close?", ["yes","no"])    
    ]

def goodbye(msg, update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text='There is Hope.. You are not alone..\n Help is always just one step away!!')
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id, text='For further help please refer to below links or do not hesitate to reachout a medical professional - \n\n  - (WHO) https://www.who.int/mental_health/management/depression/wfmh_paper_depression_wmhd_2012.pdf  \n -(MoH Singapore) https://www.moh.gov.sg/docs/librariesprovider4/guidelines/depression-cpg_r14_final.pdf')
    time.sleep(2)
    context.bot.send_message(chat_id=update.message.chat_id, text='Or you can always reach-out to us for any further questions :-) take care!')
    changeDialogState("greeting")
    return ''

def q_a_bert(msg, update: Update, context: CallbackContext):
    ans = bert_question_copy.question_answer(msg, bert_kb[0])
    context.bot.send_message(chat_id=update.message.chat_id, text=ans)

from random import randint
user_ans=[]
def surveyQueAns(update: Update, context: CallbackContext, idx):
        context.bot.send_message(chat_id=update.message.chat_id, text=base_que)
        time.sleep(TI)
        
        button=user_que[idx]
        ss_index[0]=idx
        add_suggested_actions(update, context, button)
        
        
def add_suggested_actions(update, context, response):
    options = []
    for item in response.items:
        options.append(InlineKeyboardButton(item, callback_data=item))
    reply_markup = InlineKeyboardMarkup([options])
    update.message.reply_text(response.message, reply_markup=reply_markup)

def changeDialogState(nextState):
    print("before DS=", dialog_state[0])
    dialog_state[0]=nextState
    ss_index[0]=ss_index[0] + 1
    print("after DS=", dialog_state[0])

#Function to start the bot,initiated on /start command
def controller(update: Update, context: CallbackContext):
    msg=update.message.text
    print("message sent by user:",msg, ", dialogState=", dialog_state[0],"ss_index=",ss_index[0])
    
    if(dialog_state[0].endswith("greeting")):
        greeting_section(msg,update,context)
        return ''
    elif(dialog_state[0].endswith("survey")):
        if(msg.endswith("end survey")):
            changeDialogState("q_a_c")
            context.bot.send_message(chat_id=update.message.chat_id, text='Thank you for your response(s). Next we can look at our virtual counseller - do you any question in your mind?')
        elif(ss_index[0]==0):
            surveyQueAns(update,context,1)
        elif(ss_index[0]==1):
            surveyQueAns(update,context,2)      
        elif(ss_index[0]==2):
            surveyQueAns(update,context,3)
        elif(ss_index[0]==3):
            surveyQueAns(update,context,4)
        elif(ss_index[0]==4):
            surveyQueAns(update,context,5)
        elif(ss_index[0]==5):
            surveyQueAns(update,context,6)
        elif(ss_index[0]==6):
            surveyQueAns(update,context,7)
        else:
            changeDialogState("q_a_c")
            context.bot.send_message(chat_id=update.message.chat_id, text='Thank you for your response(s). Next we can look at our virtual counseller - do you any question in your mind?')
            
        return ''
    elif(dialog_state[0].endswith("q_a_c")):
        if (msg.endswith("lonliness")):
            print("inside lonliness")
            context.bot.send_message(chat_id=update.message.chat_id, text='Sorry, we could not find any counseller ans for this. Extracting info from Knowledge base to help you further..')
            time.sleep(TI)
            changeDialogState("q_a_b")
            q_a_bert(msg, update,context)

        ans = faq_copy.getAns(msg)
        context.bot.send_chat_action(chat_id=update.effective_user.id, action=telegram.ChatAction.TYPING)
        #print("ans sim=" , ans[0])
        if (ans[0] < 0.9):
            context.bot.send_message(chat_id=update.message.chat_id, text='Sorry, we could not find any counseller ans for this. Extracting info from Knowledge base to help you further..')
            time.sleep(TI)
            changeDialogState("q_a_b")
            q_a_bert(msg, update,context)
        else :
            context.bot.send_message(chat_id=update.message.chat_id, text=ans[1])
        return ''
    elif(dialog_state[0].endswith("q_a_b")):
        if(msg.endswith("quit")):
            changeDialogState("goodbye")
            goodbye(msg, update,context)
        else: 
            q_a_bert(msg, update,context)
        return ''
    elif(dialog_state[0].endswith("goodbye")):
        goodbye(msg, update,context)    
        return ''



#function for doc search
#def q_a(bot,update):
#    msg=update.message.text
#    print("message sent by user",msg)
#    if(msg=="doc"):
#     return ''

#    ans = tfidf_doc_search.docdocsim("file_onw.txt", "file_two.txt")
#    bot.send_chat_action(chat_id=update.effective_user.id, action=telegram.ChatAction.TYPING)

#    if ans == 'NONE':
#        bot.send_message(chat_id=update.message.chat_id, text='Sorry, I could not help with this yet. Please ask something else.')
#    else :
#        bot.send_message(chat_id=update.message.chat_id, text=ans)
#def bert_qa(bo):
#    text = """New York (CNN) -- More than 80 Michael Jackson collectibles -- including the late pop star's famous rhinestone-studded glove from a 1983 performance -- were auctioned off Saturday, reaping a total $2 million. Profits from the auction at the Hard Rock Cafe in New York's Times Square crushed pre-sale expectations of only $120,000 in sales. The highly prized memorabilia, which included items spanning the many stages of Jackson's career, came from more than 30 fans, associates and family members, who contacted Julien's Auctions to sell their gifts and mementos of the singer. Jackson's flashy glove was the big-ticket item of the night, fetching $420,000 from a buyer in Hong Kong, China. Jackson wore the glove at a 1983 performance during \"Motown 25,\" an NBC special where he debuted his revolutionary moonwalk. Fellow Motown star Walter \"Clyde\" Orange of the Commodores, who also performed in the special 26 years ago, said he asked for Jackson's autograph at the time, but Jackson gave him the glove instead. "The legacy that [Jackson] left behind is bigger than life for me,\" Orange said. \"I hope that through that glove people can see what he was trying to say in his music and what he said in his music.\" Orange said he plans to give a portion of the proceeds to charity. Hoffman Ma, who bought the glove on behalf of Ponte 16 Resort in Macau, paid a 25 percent buyer's premium, which was tacked onto all final sales over $50,000. Winners of items less than $50,000 paid a 20 percent premium."""
#    question = "Where was the Auction held?"
#    ans=bert_question.question_answer(question, text)
#    print(ans)
    
    
def main():
    #updater.dispatcher.add_handler(CommandHandler(start))
  #  updater.dispatcher.add_handler(CommandHandler('bert',bert_qa))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, controller),group=1)
    updater.start_polling()

main()
