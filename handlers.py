from glob import glob
import os
from random import choice



from utils import is_cat, main_keyboard, play_random_numbers, get_bot_number, cat_rating_inline_keyboard



def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text("HELLO", reply_markup=main_keyboard())
