import json

import vk
import vkapi
import vk_api
import vk_addon
import random
import time
import requests
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# Импорт Библиотек

from ConsoleCmds import *
from Parser import *
from TrojanCommands.CreatorCmds import Commands
from TrojanCommands.message import message
from Settings import *
from Keyboard import *
from Method import *
from DT import *
from WebHook import *


# Импорт Модулей

# Meow
# Кот написан на python, так как разработчику не хватило конфеток на нормальный сервер, то заместо базы данных используются Json Файлы, в которых
# Хранится информация о пользователях, чатах и т.п
# Сам код написан относительно криво и присутвуют некоторые ошибки, но в ближайшее время мы их исправим)

def main():
    CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

    try:
        vk_session = vk_api.VkApi(
            token='ваш токен')
        # Получение токена

        longpoll = VkBotLongPoll(vk_session, 'айди группы')
        f_toggle: bool = False

        cmd = ['!meow']
        # Список команд(спрятано)

        for event in longpoll.listen():
            # Обращаемся к вк
            user = event.obj.message['from_id']

            def text(num):
                if num == 1:
                    return event.obj.message['text'].split()[0].lower()
                  # первая строка сообщения
                elif num == 2:
                    b = event.obj.message['text'].split()[1].find('|')
                    return event.obj.message['text'].split()[1][3:b]
                  # получаем айди из [id0|meow]
                elif num == 3:
                    return ' '.join(event.obj.message['text'].split()[1:])
                  # оставшиеся строки текста

            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                # Получаем сообщения из чата, не из лс!
                if text(1) in cmd:
                    JS.Prof_Creat(event, user)
                    # Проверяем существует ли такой пользователь и был ли создан для него профиль
                    JS.chat_create(event)
                    # Проверяем существует ли такой чат и был ли создан для него профиль

                    met.commands(user, event, text(1), text(3))

                if Chats.action(event) == True:
                  # Получаем айди приглашенных пользователей.
                    pass




            elif event.type == VkBotEventType.MESSAGE_EVENT:
                # если это одно из 3х встроенных действий:
                if event.object.payload.get('type') in CALLBACK_TYPES:
                    # отправляем серверу указания как какую из кнопок обработать.
                    r = vk.messages.sendMessageEventAnswer(
                        event_id=event.object.event_id,
                        user_id=event.object.user_id,
                        peer_id=event.object.peer_id,
                        event_data=json.dumps(event.object.payload))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception:
            time.sleep(240)
            pass
