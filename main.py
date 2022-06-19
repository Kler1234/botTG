import telebot
import config
from telebot import types
#import requests
import random
import covid
import pydantic
from covid import Covid

#token
bot = telebot.TeleBot(config.TOKEN)

#starting bot
@bot.message_handler(commands = ['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width = 2) #keyboard
    item1 = types.KeyboardButton("Информация📕")
    item2 = types.KeyboardButton("Рандомное число🎲")
    item3 = types.KeyboardButton("Как дела?👁")
    item5 = types.KeyboardButton("COVID19🌎")

    markup.add(item1, item2, item3, item5)

#send sticker
    sticker = open('E:/bot/sticker/hello.png', 'rb')
    bot.send_sticker(message.chat.id, sticker)
#start message

    bot.send_message (message.chat.id, 'Привет, {0.first_name}! \nЯ бот по имени {1.first_name}\n'.format(message.from_user, bot.get_me()),
        parse_mode = 'html', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Информация📕":
            bot.send_message(message.chat.id,'Я - бот по имени CollegePractice!\nЯ есть подопытный кролик 🐇')
        elif message.text == "Рандомное число🎲":
            bot.send_message(message.chat.id, str(random.randint(0,100)) + " 🎲")
        elif message.text == "Как дела?👁":
            markup = types.InlineKeyboardMarkup(row_width = 2)
            inline1 = types.InlineKeyboardButton("Хорошо!😄", callback_data = "good")
            inline2 = types.InlineKeyboardButton("Не очень 😢", callback_data = "bad")

            markup.add(inline1, inline2)

            bot.send_message(message.chat.id, 'Отлично!😄\nУ тебя как?', reply_markup=markup)
        elif message.text == "COVID19🌎":
            markupn = types.InlineKeyboardMarkup(row_width = 2)
            inline5 = types.InlineKeyboardButton("США", callback_data = "US")
            inline6 = types.InlineKeyboardButton("Россия", callback_data = "rus")
            inline7 = types.InlineKeyboardButton("Беларусь", callback_data = "bel")
            inline8 = types.InlineKeyboardButton("Украина", callback_data = "ukr")
            markupn.add(inline5, inline6, inline7, inline8)
            bot.send_message(message.chat.id, "Выберите местность", reply_markup=markupn)
        else:
            bot.send_message(message.chat.id, 'Я не знаю, что на это ответить 😢')
    else:
    	bot.send_message(message.chat.id, 'Я не знаю, что на это ответить(')

@bot.callback_query_handler(func = lambda call:True)
def callback_inline(call):
    try:
        if call.data == "good":
            bot.send_message(call.message.chat.id, "Вот и отличненько 😊")
        elif call.data == "bad":
            bot.send_message(call.message.chat.id, "Бывает 😢\nДержись!")

        if call.data == "US":
                covid = Covid(source="worldometers")
                location = covid.get_status_by_country_name("USA")
                bot.send_message(call.message.chat.id, f"Данные по США 🇺🇸:\nЗаболевших: {location['confirmed']}\nВыличившихся: {location['recovered']}\nУмерших: {location['deaths']}\nЗаболевших за сутки: {location['new_cases']} ""\n\n\n\n\n\n\n\n")
        elif call.data == "rus":
                covid = Covid(source="worldometers")
                location = covid.get_status_by_country_name("russia")
                bot.send_message(call.message.chat.id, f"Данные по России 🇷🇺:\nЗаболевших: {location['confirmed']}\nВыличившихся: {location['recovered']}\nУмерших: {location['deaths']}\nЗаболевших за сутки: {location['new_cases']} ""\n\n\n\n\n\n\n\n")
        elif call.data == "bel":
                covid = Covid(source="worldometers")
                location = covid.get_status_by_country_name("belarus")
                bot.send_message(call.message.chat.id, f"Данные по Беларуси 🇧🇾:\nЗаболевших: {location['confirmed']}\nВыличившихся: {location['recovered']}\nУмерших: {location['deaths']}\nЗаболевших за сутки: {location['new_cases']} ""\n\n\n\n\n\n\n\n")
        elif call.data == "ukr":
                covid = Covid(source="worldometers")
                location = covid.get_status_by_country_name("ukraine")
                bot.send_message(call.message.chat.id, f"Данные по Украине 🇺🇦:\nЗаболевших: {location['confirmed']}\nВыличившихся: {location['recovered']}\nУмерших: {location['deaths']}\nЗаболевших за сутки: {location['new_cases']} ""\n\n\n\n\n\n\n\n")      
        else:
                covid = Covid(source="worldometers")
                covid.get_data()
                bot.send_message(call.message.chat.id, f"Данные по Миру:\nЗаболевших: {location['confirmed']}\nВыличившихся: {location['recovered']}\nУмерших: {location['deaths']}\nЗаболевших за сутки: {location['new_cases']} ""\n\n\n\n\n\n\n\n")
    except Exception as e:
    	pass
bot.polling(none_stop = True)
