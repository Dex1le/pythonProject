import telebot
from telebot import types
import konfig

bot = telebot.TeleBot("5690685783:AAGgnl3RFqYuv8uUVIzN-CInVdc4hHRVuqY")

# -------------------------------------------------------------------------------------------------------------------- #
'''@bot.message_handler(commands=['start'])
def start_command(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Создать список дел 📝')
    markup1.add(item1)

    bot.send_message(message.chat.id, "<b>Привет, я бот тайм-менджмента, давай составим твой список дел!</b>",
                     parse_mode='html', reply_markup=markup1)
# -------------------------------------------------------------------------------------------------------------------- #
@bot.message_handler(content_types=['text'])
def new(message):
    if message.text == 'Создать список дел 📝':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('📕 1-3')
        item3 = types.KeyboardButton('📗 4-6')
        item4 = types.KeyboardButton('📘 7-10')
        markup2.add(item2, item3, item4)
        bot.send_message(message.chat.id, "<b>Выбери количество дел!</b>", parse_mode='html', reply_markup=markup2)

    elif message.text == '📕 1-3':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton('1️⃣')
        item6 = types.KeyboardButton('2️⃣')
        item7 = types.KeyboardButton('3️⃣')
        item15 = types.KeyboardButton('🔙')
        markup3.add(item5, item6, item7)
        markup3.add(item15)
        bot.send_message(message.chat.id, "<b>Выбери дело 😇</b>", parse_mode='html', reply_markup=markup3)

    elif message.text == '📗 4-6':
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item8 = types.KeyboardButton('4️⃣')
        item9 = types.KeyboardButton('5️⃣')
        item10 = types.KeyboardButton('6️⃣')
        item15 = types.KeyboardButton('🔙')
        markup4.add(item8, item9, item10)
        markup4.add(item15)
        bot.send_message(message.chat.id, "<b>Выбери дело 😇</b>", parse_mode='html', reply_markup=markup4)


    elif message.text == '📘 7-10':
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item11 = types.KeyboardButton('7️⃣')
        item12 = types.KeyboardButton('8️⃣')
        item13 = types.KeyboardButton('9️⃣')
        item14 = types.KeyboardButton('🔟')
        item15 = types.KeyboardButton('🔙')
        markup5.add(item11, item12)
        markup5.add(item13, item14)
        markup5.add(item15)
        bot.send_message(message.chat.id, "<b>Выбери дело 😇</b>", parse_mode='html', reply_markup=markup5)

    elif message.text == '🔙':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('📕 1-3')
        item3 = types.KeyboardButton('📗 4-6')
        item4 = types.KeyboardButton('📘 7-10')
        markup2.add(item2, item3, item4)
        bot.send_message(message.chat.id, "<b>Выбери количество дел!</b>", parse_mode='html', reply_markup=markup2)'''

# -------------------------------------------------------------------------------------------------------------------- #
@bot.message_handler(commands=['1️⃣'])
def reply(message):
    sent = bot.reply_to(message, 'Напиши своё дело:')
    bot.register_next_step_handler(sent, delo)

def delo(message):
    message_to_save = message.text
    bot.send_message(message.chat.id, message_to_save)

bot.infinity_polling()