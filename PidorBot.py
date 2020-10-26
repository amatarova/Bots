import requests
import telebot
from telebot import types
import config

token = "1328156843:AAHvRBpmctDwmNqc_GOgN1-S5g6PEx87Pmo"

bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('start', '/more')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! У меня для тебя инструкции: "
                                      "я умею обзываться и хвалить, но нужно, "
                                      "чтобы сообщение начиналось с 'Я' или 'Ты'. "
                                      "Для других инструкций "
                                      "введи /more"
                     , reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def send_next(message):
    if message.text.lower().startswith('ты'):
        bot.send_message(message.chat.id, 'Сам ты' + message.text[2:])
    if message.text.lower().startswith('я'):
        if message.text.endswith('ю') or message.text.endswith('у'):
            bot.send_message(message.chat.id, 'Да, ты' + message.text[1:-1] + 'ешь')
        else:
            bot.send_message(message.chat.id, 'Да, ты' + message.text[1:])
    if message.text == "/more":
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row('300')
    if message.text == "300":
        bot.send_message(message.chat.id, "Отсоси у тракториста :D")
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, "Пидора ответ")

def good_news(message):
    if message.text.lower()('новость'):
        receive = requests.get("https://ria.ru/khoroshie-novosti/")


if __name__ == '__main__':
    bot.polling(none_stop=True)
