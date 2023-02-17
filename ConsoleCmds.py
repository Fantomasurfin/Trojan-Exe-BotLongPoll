import vk
from TrojanCommands import message


class chat:
    # Управление чатом через консоль, удобная вещь, если хочешь побаловаться, но по факту вовсе не нужна вашему боту)
    def __init__(self):
        pass

    def open():
        start = input('Добро пожаловать, Аноним Анонимус! Для получения списка команд введите !help')
        print(f"Chats:\n !Send")

    def consmsg():
        user_input = input('Отправка в чат')
        if '!Send' in str(user_input):
            message.message.msg(chat=None, peer_id=int(user_input[7:9]) + 2000000000, message=str(user_input[10:]),
                                attachment=None, keyboard=None, sticker=None)
