import telebot
# from models import TestMath
from dotenv import load_dotenv
import os
import random

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, "Hello!..")

global_score = 0
@bot.message_handler(commands=['test'])
def askquestion(message):
    score = 0
    # bot.send_message(input(num1 = random.randint(1,500)))
    # bot.send_message(input(num2 = random.randint(1,500)))
    num1 = random.randint(1,500)
    num2 = random.randint(1,500)
    correctanswer = num1+num2
    answer = bot.send_message(message.chat.id, str(num1)+"+"+str(num2)+"=")
    if int(answer) == correctanswer:
        bot.send_message(message.chat.id, "To'g'ri javob!")
        score = score + 10
    else:
        bot.send_message(message.chat.id, "Yana bir marta unib ko'ring!..")
    return (score)
        
@bot.message_handler(commands=['result'])
def send_answer(message):
    global_score = global_score + askquestion()
    global_score = global_score + askquestion()
    global_score = global_score + askquestion()
    global_score = global_score + askquestion()

    bot.send_message(message.chat.id, f'Umumiy Ball {global_score}')

bot.infinity_polling()