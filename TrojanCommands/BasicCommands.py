import random

import vk

from DT import JS
from Keyboard import Keyboard
from TrojanCommands import message
from Settings import *
from Parser import *


# В разработке
class Basics:
    def __init__(self, event, text):
        self.event = event
        self.text = text

    # Функция исключение пользователя по айди
    # member_Id - айди участника, которого вы хотите исключить
    # user_Id - айди участника, который будет исключать указанного пользователя
    def kick(event, member):
        try:
            vk_session.method("messages.removeChatUser",
                              {"chat_id": event.chat_id, "user_id": event.obj.message['from_id'], "member_id": member})
        except:
            pass

    # Функция для бана пользователя по айди
    def ban(event, member):
        if member in JS.Value('Проверяем, есть ли пользователь в списке забаненных'):
            message.message.msg(None, event.chat_id + 2000000000,
                                f'Сожалею, но данный пользователь уже в бане, могу предложить лишь забанить самого себя!',
                                'video300887461_456239987', None, None)
        else:
            message.message.msg(None, event.chat_id + 2000000000,
                                f'Ты думал я *id{member}(тебя) не переиграю?! Я знаю все твои шаги наперед!!! ЗАБАНЕН',
                                'video300887461_456239987', None, None)
            Basics.kick(event, member)
            JS.New_Value_List('Добавляем пользователя в список забаненных')

    # Делает бабах и кикает весь чат.
    def kaboom(event):
        for i in Users.Profiles(event):
            try:
                Basics.kick(event, i['id'])
            except:
                pass

    # Скидывает рандомный арт
    def Arts(event, art):
        if art == '!япония':
            message.message.msg(None, event.chat_id + 2000000000, 'Держи красивый арт с японией',
                                f'photo-айди альбома_{random.randint()}', None, None)
