import vk
from vk_api.utils import get_random_id
from Settings import *


class message:
    def __init__(self, chat, peer_id, message, attachment, keyboard, sticker, conv, cmids):
        self.group_id = 204691208
        self.chat = chat
        self.peer_id = peer_id
        self.message = message
        self.attachment = attachment
        self.keyboard = keyboard
        self.sticker = sticker
        self.conv = conv
        self.cmids = cmids

    def msg(chat, peer_id, message, attachment, keyboard, sticker):
        vk.messages.send(
            chat_id=chat,
            peer_id=peer_id,
            message=message,
            attachment=attachment,
            keyboard=keyboard,
            sticker_id=sticker,
            random_id=0
        )

    # Функция для отправки сообщения/стикера/арта/клавиатуры

    def emsg(peer_id, message, attachment, conv, keyboard):
        vk.messages.edit(
            peer_id=peer_id,
            message=message,
            attachment=attachment,
            conversation_message_id=conv,
            keyboard=keyboard
        )

    # Функция для редактирования сообщения/арта

    def dmsg(message_id, peer_id, cmids):
        vk.messages.delete(
            message_ids=message_id,
            delete_for_all=1,
            peer_id=peer_id,
            cmids=cmids
        )

    # Функция для удаления сообщения/арта/стикера

    def cmsg(self):
        vk.messages.startCall(
            group_id=self.group_id
        )
    # Функция для создания звонка в чате, работает только в беседах, созданных не в сообществе
