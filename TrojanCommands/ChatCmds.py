import vk

from Keyboard import Keyboard
from TrojanCommands import message
from Parser import *
from DT import *
from Keyboard import *

# Класс для работы с базой данных чата и изменения его настроек/вывод сообщний с информацией о чате
class Cht:
    def info(event):
        message.msg(None, event.chat_id + 2000000000, f"""
Приветики~ добро пожаловать в профиль вашего чата:

оформление вашей команды

                 """, 'айди фото', None, None)

# Класс для работы с базой данных сетки и изменение ее настройки.
class Set:
    def info(event):
        message.msg(None, event.chat_id + 2000000000, f"""
💮 Хай~ хай, хочешь поглазеть на Информацию о своей сеточке?

оформление вашей команды
                         """, 'айди фото', None, None)
