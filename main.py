print('Загрузка программы...') 
import telebot 
from telebot import types 
import sqlite3 
bot = telebot.TeleBot('5418533436:AAHulotrkbczRAPkOn1TkIAMVXFdu4M6kBQ') 
conn = sqlite3.connect('data.db', check_same_thread=False) 
cur = conn.cursor() 
print('Бот запущен!') 

array = [
    ['Рука помощи ','Животные','https://pitomec58.com/'],
    ['Живой', 'Попавшим в беду', 'https://livefund.ru/'],
    ['Старость в радость ','Пенсионеры','https://starikam.org/'],
    ['Дари Заботу', 'инвалиды', 'https://vk.com/darizabotu'],
    ['РЕЙ', 'Животные', 'https://rayfund.ru/'],
    ['Всем Миром', 'Животные', 'https://fond-vsem-mirom.ru/'],
    ['Ночлежка', 'Попавшим в беду', 'https://homeless.ru/'],
    ['Солидарность', 'Попавшим в беду', 'https://solidarnost.su/'],
    ['София', 'Пенсионеры', 'https://sofiafond.ru/'],
    ['ДОВЕРИЕ', 'Пенсионеры', 'https://pansionat.life/'],
    ['Движение Вверх', 'инвалиды', 'https://movementup.ru/'],
    ['Новая Жизнь', 'инвалиды', 'http://www.fondnewlife.ru']
]

def controler_keyboard(name_kb): 
    if name_kb == 'main': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        b1 = types.KeyboardButton('Пожертвовать в фонд благотворительности') 
        markup.add(b1) 
        return markup
 
    if name_kb == 'kap': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        b1 = types.KeyboardButton('В фонд животных') 
        b2 = types.KeyboardButton('В фонд попавшим в беду') 
        b3 = types.KeyboardButton('В фонд пенсионеров')
        b4 = types.KeyboardButton('В фонд инвалидов')
        markup.add(b1) 
        markup.add(b2, b3, b4) 
        return markup 

@bot.message_handler(commands=['start']) 
def start(message): 
    uid = message.chat.id 
    name = message.from_user.first_name 
    bot.send_message(uid, 'Приветствуем на нашем боте по помощи поиска благотворительных фондов👋! \nДля начала работы бота нажмите на кнопку:👇', reply_markup=controler_keyboard('main'))
 

@bot.message_handler(content_types=['text']) 
def main_controler(message): 
    uid = message.chat.id 
    name = message.from_user.first_name 

    if message.text == 'Пожертвовать в фонд благотворительности' :
        bot.send_message(uid, 'Укажите направления фонда 👇', reply_markup=controler_keyboard('kap'))

    if message.text == 'В фонд животных':
        for arr in array:
            if arr[1] == 'Животные' :
                bot.send_message(uid, arr[2], reply_markup=controler_keyboard('kap'))
  
    if message.text == 'В фонд попавшим в беду':
        for arr in array:
            if arr[1] == 'Попавшим в беду' :
                bot.send_message(uid, arr[2], reply_markup=controler_keyboard('kap'))

    if message.text == 'В фонд пенсионеров':
        for arr in array:
            if arr[1] == 'Пенсионеры' :
                bot.send_message(uid, arr[2], reply_markup=controler_keyboard('kap'))
    
    if message.text == 'В фонд инвалидов':
        for arr in array:
            if arr[1] == 'инвалиды' :
                bot.send_message(uid, arr[2], reply_markup=controler_keyboard('kap'))

bot.infinity_polling()


