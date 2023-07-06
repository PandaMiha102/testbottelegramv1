import os
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot(os.environ.get('BOT_API_KEY'))

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

exercises = [
    ('Chest.m', 'https://www.youtube.com/watch?v=Vf2evnGKTfo'),
    ('Back.m', 'https://www.youtube.com/watch?v=ni4qZejmb3I'),
    ('Arms.m', 'https://www.youtube.com/watch?v=NsHsuqd-B2Y'),
    ('Legs.m', 'https://www.youtube.com/watch?v=KF6_2hRFtq4'),
    ('Shoulders.m', 'https://www.youtube.com/watch?v=0N_SmoM3UQc')
]

for exercise in exercises:
    cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES (?, ?)", exercise)
    print(cursor)
    
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привітатися!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привіт! Я фітнес бот.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Привітатися!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Добре')
        btn2 = types.KeyboardButton('Погано')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Як себе почуваєте?', reply_markup=markup) #ответ бота
    
    if message.text == 'Добре':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Чоловік')
        btn2 = types.KeyboardButton('Жінка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Ваша стать?', reply_markup=markup) #ответ бота
    
    if message.text == 'Погано':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        bot.send_message(message.from_user.id, 'Значить сьогодні вам варто відпочити або зробити кардіо 20 хвилин', reply_markup=markup) #ответ бота
                    
    if message.text == 'Чоловік':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Chest.m')
        btn2 = types.KeyboardButton('Back.m')
        btn3 = types.KeyboardButton('Arms.m')
        btn4 = types.KeyboardButton('Legs.m')
        btn5 = types.KeyboardButton('Shoulders.m')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Що будемо тренувати?', reply_markup=markup) #ответ бота
        
    if message.text == 'Жінка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Chest.w')
        btn2 = types.KeyboardButton('Back.w')
        btn3 = types.KeyboardButton('Arms.w')
        btn4 = types.KeyboardButton('Legs.w')
        btn5 = types.KeyboardButton('Shoulders.w')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Що будемо тренувати?', reply_markup=markup) #ответ бота
    
        
        
    elif message.text == 'Chest.m':
        exercise_name = 'Chest.m'
        video_link = None

        for exercise in exercises:
            if exercise[0] == exercise_name:
                video_link = exercise[1]
                break
        bot.send_message(message.from_user.id, video_link, parse_mode='Markdown')

    elif message.text == 'Back.m':
        exercise_name = 'Back.m'
        video_link = None

        for exercise in exercises:
            if exercise[0] == exercise_name:
                video_link = exercise[1]
                break
        bot.send_message(message.from_user.id, video_link, parse_mode='Markdown')
        
    elif message.text == 'Arms.m':
        exercise_name = 'Arms.m'
        video_link = None
        
        for exercise in exercises:
            if exercise[0] == exercise_name:
                video_link = exercise[1]
                break
        bot.send_message(message.from_user.id, video_link, parse_mode='Markdown')
         
    elif message.text == 'Legs.m':
        exercise_name = 'Legs.m'
        video_link = None
        
        for exercise in exercises:
            if exercise[0] == exercise_name:
                video_link = exercise[1]
                break
        bot.send_message(message.from_user.id, video_link, parse_mode='Markdown')
          
    elif message.text == 'Shoulders.m':
        exercise_name = 'Shoulders.m'
        video_link = None

        for exercise in exercises:
            if exercise[0] == exercise_name:
                video_link = exercise[1]
                break
        bot.send_message(message.from_user.id, video_link, parse_mode='Markdown')
               
    elif message.text == 'Chest.w':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')

    elif message.text == 'Back.w':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')
        
    elif message.text == 'Arms.w':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')   
         
    elif message.text == 'Legs.w':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')  
          
    elif message.text == 'Shoulders.w':
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')
        
    
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть