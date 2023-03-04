import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Привет! Чтобы начать работу введите через пробел команду боту в формате:\n <имя валюты>\n \
<в какую валюту перевести>\n \
<количество валюты>\nЧтобы увидеть список всех доступных валют отправьте команду: /values \n \
для повторного получения подсказки отправьте команду: /help \n \
P.S. Не отправляйте боту войсы и фото'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Некорректные параметры запроса!')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Без фото пожалуйста')


@bot.message_handler(content_types=['voice', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Голос я не понимаю')


bot.polling(none_stop=True)
