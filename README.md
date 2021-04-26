## Оглавление


- [English](#English)
- [Russian](#Russian)

<a name="English"></a> 

import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from db import engine, Post
from sqlalchemy.orm import sessionmaker

logging.basicConfig(filename='bot.log', level=logging.INFO)
Session = sessionmaker(bind=engine)
session = Session()
current_step = 0


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("posts", get_posts, pass_args=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Показать новые обьявления)$'), get_posts))
    dp.add_handler(MessageHandler(Filters.regex('^(Следующие 3 новых обьявления)$'), get_posts))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал!!!")
    mybot.start_polling()
    mybot.idle()


def greet_user(update, context):
    global current_step
    current_step = 0
    print("!!! Вызван /start")
    start_text = """
    Привет. Я помогу найти тебе квартиру)

    Выберите действие:
    💡 На каждом этапе можно отправить команду /start для возвращения к этому меню.
    """
    update.message.reply_text(start_text, reply_markup=main_keyboard())


def main_keyboard():
    return ReplyKeyboardMarkup([['Показать новые обьявления']])
def next_keyboard():
    return ReplyKeyboardMarkup([['Следующие 3 новых обьявления']])


def talk_to_me(update, context):
    update.message.reply_text("Я Бот. Чтобы продолжить поиск, нажмите на кнопку снизу", reply_markup=main_keyboard())


def get_posts(update, context):
    global current_step
    global session
    global num_records
    current_offset = current_step*3
    current_step = current_step + 1
    num_records = session.query(Post).order_by(Post.id).count()
    user_text = update.message.text
    print(user_text)
    for instance in session.query(Post).order_by(Post.id).filter(Post.id >= current_offset).limit(3).all():
        print(instance)
        update.message.reply_text(str(instance))
    if current_step*3 < float(num_records):
        update.message.reply_text("Хотите посмотреть еще?", reply_markup=next_keyboard())
    else:
        update.message.reply_text("Вы посмотрели все обьявления.", reply_markup=main_keyboard())
        current_step = 0


if __name__ == "__main__":
    main()


import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from db import engine, Post
from sqlalchemy.orm import sessionmaker

logging.basicConfig(filename='bot.log', level=logging.INFO)
Session = sessionmaker(bind=engine)
session = Session()
current_step = 0


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("posts", get_posts, pass_args=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Показать новые обьявления)$'), get_posts))
    dp.add_handler(MessageHandler(Filters.regex('^(Следующие 3 новых обьявления)$'), get_posts))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал!!!")
    mybot.start_polling()
    mybot.idle()


def greet_user(update, context):
    global current_step
    current_step = 0
    print("!!! Вызван /start")
    start_text = """
    Привет. Я помогу найти тебе квартиру)

    Выберите действие:
    💡 На каждом этапе можно отправить команду /start для возвращения к этому меню.
    """
    update.message.reply_text(start_text, reply_markup=main_keyboard())


def main_keyboard():
    return ReplyKeyboardMarkup([['Показать новые обьявления']])
def next_keyboard():
    return ReplyKeyboardMarkup([['Следующие 3 новых обьявления']])


def talk_to_me(update, context):
    update.message.reply_text("Я Бот. Чтобы продолжить поиск, нажмите на кнопку снизу", reply_markup=main_keyboard())


def get_posts(update, context):
    global current_step
    global session
    global num_records
    current_offset = current_step*3
    current_step = current_step + 1
    num_records = session.query(Post).order_by(Post.id).count()
    user_text = update.message.text
    print(user_text)
    for instance in session.query(Post).order_by(Post.id).filter(Post.id >= current_offset).limit(3).all():
        print(instance)
        update.message.reply_text(str(instance))
    if current_step*3 < float(num_records):
        update.message.reply_text("Хотите посмотреть еще?", reply_markup=next_keyboard())
    else:
        update.message.reply_text("Вы посмотрели все обьявления.", reply_markup=main_keyboard())
        current_step = 0


if __name__ == "__main__":
    main()


<a name="Russian"></a> 
# Бот для поиска обьявлений об аренде жилья

На Хабре, да и не только, про ботов рассказано уже так много, что даже слишком. Но заинтересовавшись пару недель назад данной темой, найти нормальный материал у меня так и не вышло: все статьи были либо для совсем чайников и ограничивались отправкой сообщения в ответ на сообщение пользователя, либо были неактуальны. Это и подтолкнуло меня на написание статьи, которая бы объяснила такому же новичку, как я, как написать и запустить более-менее осмысленного бота (с возможностью расширения функциональности).

Часть 1: Регистрация бота

Самая простая и описанная часть. Очень коротко: нужно найти бота @BotFather, написать ему /start, или /newbot, заполнить поля, которые он спросит (название бота и его короткое имя), и получить сообщение с токеном бота и ссылкой на документацию. Токен нужно сохранить, желательно надёжно, так как это единственный ключ для авторизации бота и взаимодействия с ним.

Часть 2: Подготовка к написанию кода

Как уже было сказано в заголовке, писать бота мы будем на Python'е. В данной статье будет описана работа с библиотекой PyTelegramBotAPI (Telebot). Если у вас не установлен Python, то сперва нужно сделать это: в терминале Linux нужно ввести

sudo apt-get install python python-pip


Если же вы пользуетесь Windows, то нужно скачать Python с официального сайта .

После, в терминале Linux, или командной строке Windows вводим

pip install pytelegrambotapi


Теперь все готово для написания кода.

Часть 3: Получаем сообщения и говорим «Привет»

Небольшое отступление. Телеграмм умеет сообщать боту о действиях пользователя двумя способами: через ответ на запрос сервера (Long Poll), и через Webhook, когда сервер Телеграмма сам присылает сообщение о том, что кто-то написал боту. Второй способ явно выглядит лучше, но требует выделенного IP-адреса, и установленного SSL на сервере. В этой статье я хочу рассказать о написании бота, а не настройке сервера, поэтому пользоваться мы будем Long Poll'ом.

Открывайте ваш любимый текстовый редактор, и давайте писать код бота!

Первое, что нужно сделать это импортировать нашу библиотеку и подключить токен бота:

import telebot;
bot = telebot.TeleBot('%ваш токен%');
