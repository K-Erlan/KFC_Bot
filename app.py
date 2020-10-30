# KFC_Bot
# This bot is advertising the KFC products. Booking the fastfood from the internet is becoming more easier and better.

import telebot
from telebot import types
# Global bot setting
TOKEN = '1196444645:AAGNtPrJjBG0fYV1kBQcHDA0UwEXJpFGONY'

# Code
PRODUCTS = {}
print('Working')
bot = telebot.TeleBot(TOKEN)


def add_category(name):
    PRODUCTS[name] = []


def add_product(to, name, price, photo):
    PRODUCTS[to].append([name, price, photo])


def get_categories_list():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for CATEGORIES in PRODUCTS:
        markup.add(CATEGORIES)
    markup.add("🆘Помощь")
    return markup


def send_products(to, category, markup):
    for X in PRODUCTS[category]:
        bot.send_photo(to,
                       X[2],
                       reply_markup=markup,
                       caption=X[0]+"\n\nЦена: "+X[1])
# Product settings

add_category("🍔Бургеры")
add_category("🌭Твистеры")
add_category("🧃Напитки")
add_product(
 "🍔Бургеры", "Чизбургер",
 "129 сом",
 "https://nambafood.kg/dish_image/55712.png")
add_product(
 "🍔Бургеры", "Лонгер",
 "69 сом",
 "https://nambafood.kg/dish_image/55049.png")
add_product(
 "🍔Бургеры", "ШефБургер оригинальный",
 "150 сом",
 "https://nambafood.kg/dish_image/97971.png")
add_product(
 "🍔Бургеры", "ШефБургер острый",
 "150 сом",
 "https://nambafood.kg/dish_image/97972.png")
add_product(
 "🍔Бургеры", "Чизбургер Де Люкс",
 "169 сом",
 "https://nambafood.kg/dish_image/97973.png")
add_product(
 "🍔Бургеры", "Шефбургер Де Люкс оригинальный",
 "189 сом",
 "https://nambafood.kg/dish_image/97974.png")
add_product(
 "🍔Бургеры", "Шефбургер Де Люкс острый",
 "189 сом",
 "https://nambafood.kg/dish_image/97975.png")
add_product(
 "🍔Бургеры", "Шефбургер Джуниор Оригинальный",
 "144 сом",
 "https://nambafood.kg/dish_image/98788.png")
add_product(
 "🍔Бургеры", "Шефбургер Джуниор Острый",
 "144 сом",
 "https://nambafood.kg/dish_image/98789.png")
add_product(
 "🌭Твистеры", "Ай-Твистер Чиз",
 "69",
 "https://nambafood.kg/dish_image/55047.png")
add_product(
 "🌭Твистеры", "Твистер из тостера оригинальный",
 "150",
 "https://nambafood.kg/dish_image/84542.png")
add_product(
 "🌭Твистеры", "Твистер из тостера острый",
 "150",
 "https://nambafood.kg/dish_image/55051.png")
add_product(
 "🌭Твистеры", "Боксмастер из тостера оригинальный",
 "210",
 "https://nambafood.kg/dish_image/97961.png")
add_product(
 "🌭Твистеры", "Боксмастер из тостера острый",
 "210",
 "https://nambafood.kg/dish_image/97962.png")
add_product(
 "🌭Твистеры", "Твистер Джуниор",
 "119",
 "https://nambafood.kg/dish_image/97963.png")
add_product(
 "🌭Твистеры", "Твистер веджи",
 "150",
 "https://nambafood.kg/dish_image/97964.png")
add_product(
 "🌭Твистеры", "Твистер де Люкс Оригинальный",
 "189",
 "https://nambafood.kg/dish_image/98786.png")
add_product(
 "🌭Твистеры", "Твистер де Люкс Острый",
 "189",
 "https://nambafood.kg/dish_image/98787.png")
add_product(
 "🌭Твистеры", "Сандерс пита",
 "199",
 "https://nambafood.kg/dish_image/99430.png")
add_product(
 "🧃Напитки", "Пепси в бутылке 0,5",
 "55",
 "https://nambafood.kg/dish_image/55055.png")
add_product(
 "🧃Напитки", "Липтон Айс Ти 0,5 - черный",
 "69",
 "https://nambafood.kg/dish_image/55073.png")
add_product(
 "🧃Напитки", "Липтон Айс Ти 0,5 - зеленый",
 "69",
 "https://nambafood.kg/dish_image/55072.png")
add_product(
 "🧃Напитки", "Милк шейк - шоколадно-ореховый 0,25",
 "90",
 "https://nambafood.kg/dish_image/55060.png")
# Bot function


@bot.message_handler(content_types=['text'])
def bot_function(message):
    mes = message.text
    markup = get_categories_list()
    if mes == "/start":
        bot.send_message(message.from_user.id,
                         "Привет "+message.from_user.first_name)
        bot.send_message(message.from_user.id,
                         "Выберите категорию",
                         reply_markup=markup)
    elif mes == "🆘Помощь":
        bot.send_message(message.from_user.id,
                         "Напишите или нажмите на ➡️'/start' ," +
                         "а так же этот бот для теста ",
                         reply_markup=markup)
    elif mes in PRODUCTS:
        send_products(message.from_user.id, mes, markup)
bot.polling(none_stop=True)
