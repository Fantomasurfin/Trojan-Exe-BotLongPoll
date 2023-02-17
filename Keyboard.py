import json

from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import os

from vk_api.utils import get_random_id

from Debbuger import *

from Settings import vk

from DT import *

settings = dict(one_time=False, inline=True)
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')


# Типы кнопок 'show_snackbar' - выводит окошко с текстовым сообщением, 'open_link' - кнопка с ссылкой, 'open_app' - выбрасывает пользователя в приложение вк


class Keyboard:
    def __init__(self, event):
        self.event = event

        # Не обращаем внимание на функцию ниже)))))))))
    def Control():
        try:
            keyboard_1 = VkKeyboard(**settings)
            # pop-up кнопка
            keyboard_1.add_callback_button(label='Пинг', color=VkKeyboardColor.POSITIVE,
                                           payload={"type": "show_snackbar", "text": '{⏳}| 1.27Сек #|# 1.87ms'})
            keyboard_1.add_line()
            keyboard_1.add_callback_button(label='CPU/RAM', color=VkKeyboardColor.NEGATIVE,
                                           payload={"type": "show_snackbar", "text": OS.CPU()})
            return (keyboard_1).get_keyboard()

        except Exception as e:
            print(e)

    # Клавиатура с ссылкой на команды
    def Documentation():
        keyboard = VkKeyboard(**settings)
        keyboard.add_callback_button(label='Команды', color=VkKeyboardColor.POSITIVE,
                                     payload={"type": "open_link", "link": "https://vk.com/tr_exe"})
        return keyboard

    # если это одно из 3х встроенных действий:

    def Payload(event, keyboard, attachment):
        f_toggle: bool = False
        last_id = vk.messages.send(
            peer_id=event.obj.peer_id,
            random_id=get_random_id(),
            keyboard=(keyboard).get_keyboard(),
            message='Держи meow 🐾...'
            , attachment=attachment)
        f_toggle = not f_toggle
