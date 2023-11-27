"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import my_settings
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_constellation(update, context):
    text = "Вызван /planet"
    my_list = update.message.text.split()
    if len(my_list) == 2:
      planet_name = my_list[1].lower()
      str_date = datetime.now().strftime("%Y/%m/%d")
      if  planet_name == "mars":
          planet = ephem.Mars(str_date)
          text = ephem.constellation(planet)
      elif planet_name == "mercury":
          planet = ephem.Mercury(str_date)
          text = ephem.constellation(planet)
      elif planet_name == "venus":
          planet = ephem.Venus(str_date)
          text = ephem.constellation(planet)
      elif planet_name == "jupiter":
          planet = ephem.Jupiter(str_date)
          text = ephem.constellation(planet)   
      elif planet_name == "saturn":
          planet = ephem.Saturn(str_date)
          text = ephem.constellation(planet)
      elif planet_name == "uranus":
          planet = ephem.Uranus(str_date)
          text = ephem.constellation(planet)   
      elif planet_name == "neptune":
          planet = ephem.Neptune(str_date)
          text = ephem.constellation(planet)   
      else:
          text = "такой планеты нет"
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(my_settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
