#
#### [English](#English) / [Russian](#Russian)

# Apartments search bot


<a name="English"></a> 

## Introduction
apartments-search-bot is Telegram bot for searching an apartments in social network vkontakte.ru (vk.com)
Bot uses SQLite database to store posts from public groups vk.com.


## Getting started

1. Clone repositary, activate env (if you want) and install requirements:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/bbossankimster/apartments-search-bot.git
cd apartments-search-bot.git
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
2. Create Telegram bot according https://t.me/botfather instructions and get a token.

3. Put your token to settings.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
API_KEY = "YOUR_API_KEY"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Basic usage

1. Run Python bot application and run bot in Telegram:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python bot.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![](media/bot.png)

<a name="Russian"></a> 

# Бот для поиска обьявлений об аренде жилья

## Описание бота

Бот показывает обьявления, которые были сохраненные в базу данных с помощью парсера групп вКонтакте.

## Начальная установка и настройка

1. Склонируйте репозистрарий, активируйте virtual env (если нелбходимо), установите зависимости и модули

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/bbossankimster/apartments-search-bot.git
cd apartments-search-bot.git
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. Создайте Телеграм бота с помощью https://t.me/botfather и получите токен

3. Добавьте токен в settings.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
API_KEY = "ВАШ ТОКЕН"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Запуск приложения

Запустите Python приложение и откройте бота в Телеграм

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python bot.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![](media/bot.png)