import telebot
import random
import openpyxl
import pandas as pd
from openpyxl import load_workbook

#advices_list = openpyxl.load_workbook(Advices.xlsx)

#adv = pd.read_excel('Advices.xlsx', sheet_name='Лист1')
#print(adv.head())
#filepath = r"C:\Users\user.COMP-512-13\Desktop\ИСИП\БлюВейл\Advices.xlsx"

adv = pd.read_excel("Advices.xlsx")
rows = adv.values.tolist()

#global adv

from telebot import types

from The_Token import API_TOKEN
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
  bot.send_message(message.chat.id, "Добро пожаловать в бота BlueWhale! \nВведите /help для предоставления большей информации")
@bot.message_handler(commands = ['help'])
def help(message: types.Message):
    bot.send_message(message.chat.id,"Привет, Я BlueWhale! Полезный бот, который будет отправлять тебе советы\
    для улучшения твоего морально состояния, а так же может быстро вывести сервисы для психологической помощи и телефон доверия!")

    keys1 = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text='Случайный совет', callback_data='random_advice_pressed')
    btn2 = types.InlineKeyboardButton(text='Контакты и сервисы', callback_data='contacts_pressed')

    keys1.add(btn1, btn2)

    bot.send_message(message.chat.id,"Для продолжения нажми одну из желаемых кнопок:", reply_markup=keys1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "random_advice_pressed":
            filepath = r"C:\Users\user.COMP-512-13\Desktop\ИСИП\БлюВейл\Advices.xlsx"
            adv = pd.read_excel(filepath)
            rows = adv.values.tolist()
            random_adv = random.choice(rows)
            bot.send_message(call.message.chat.id, "Вот ваш совет:")
            bot.send_message(call.message.chat.id, f"⭐ {str(random_adv[1])}")

            keys2 = types.InlineKeyboardMarkup()

            btn1 = types.InlineKeyboardButton(text='Случайный совет', callback_data='random_advice_pressed')
            keys2.add(btn1)

            bot.send_message(call.message.chat.id, "Получить еще совет?", reply_markup=keys2)


        elif call.data == "contacts_pressed":
            bot.send_message(call.message.chat.id, "⭐ Онлайн-сервисы:\n\nЯсно: (yasno.live) Онлайн-консультации с психологами.\
            \n\nZigmund.Online: (zigmund.online) Подбор психологов для онлайн-терапии.\
            \n\n7 Cups: (7cups.com) Чат поддержки с обученными слушателями (англ.).\
            \n\n\n📱 Телефоны доверия:\n\nОбщероссийский телефон доверия для детей, подростков и их родителей: 8-800-2000-122 (бесплатно, анонимно).\
            \n\nГорячая линия психологической помощи МЧС России: 8-800-775-17-17 (бесплатно, круглосуточно).\
            \n\nМосковская служба психологической помощи населению: 051 (с городского) или +7 (495) 051 (с мобильного).\
            \n \nВажное предупреждение: Этот бот не заменяет профессиональную помощь. При серьезных проблемах обратитесь к специалисту.")

bot.polling()