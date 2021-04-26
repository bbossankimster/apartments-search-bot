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


<a name="Russian"></a> 
# Бот для поиска обьявлений об аренде жилья

