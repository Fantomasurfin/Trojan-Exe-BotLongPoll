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
# импорт библиотек

from ConsoleCmds import *
from Parser import *
from TrojanCommands.BasicCmds import Basics
from TrojanCommands.ChatCmds import Cht
from TrojanCommands.ChatCmds import Set
from TrojanCommands.CreatorCmds import Commands
from TrojanCommands.message import message
from Settings import *
from Keyboard import *
from DT import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from TrojanCommands.Game import *
# импорт модулей


class met:
    def __init__(self, event, text):
        self.event = event
        self.text = text

    # Команды Бота, написал так, потому что switch с вк не срабатывает. Здесь залита лишь одна команда
    def commands(id, event, text, text1):
        if text == '!тест':
            message.msg(None, event.chat_id + 2000000000, 'успешно', None, None, None),

        elif text == '!профиль':
            Game.profile(event, id)

        elif text == '!чат':
            Cht.info(event)

        elif text == '!онлайн':
            message.msg(None, event.chat_id + 2000000000, Users.online_msg(event), None, None, None)

        elif text == '!оффлайн':

        elif text == '!пинг':
            message.msg(None, event.chat_id + 2000000000,
                        'Разработчик этого ужастного бота поленился написать команду для пинга! Так что предлагаем вам точную дату призыва макаронного бога!\n\n ⌛До призыва макаронного бога осталось: 99999 лет',
                        '', None, None)
        
        # Другие команды намеренно скрыты))))))))))))0
            
          
