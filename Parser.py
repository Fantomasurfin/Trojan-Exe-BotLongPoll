import vk
from Settings import *

# класс для работы с пользователями
class Users:
    def __init__(self, event):
        self.event = event

    # Получении имени пользователя через API
    def User_Name(event):
        for i in range(len(Users.Profiles(event))):
            if Users.Profiles(event)[i]["id"] == event.obj.message['from_id']:
                first_name = Users.Profiles(event)[i]["first_name"]
                last_name = Users.Profiles(event)[i]["last_name"]
                full_name = first_name + " " + last_name
                return full_name

    # Получаем имя пользователя по его айди.
    def User_Name_Id(event, id):
        for i in range(len(Users.Profiles(event))):
            if Users.Profiles(event)[i]["id"] == id:
                first_name = Users.Profiles(event)[i]["first_name"]
                last_name = Users.Profiles(event)[i]["last_name"]
                full_name = first_name + " " + last_name
                return full_name

    # Получаем всех участников бесед в json формате.
    def Profiles(event):
        Conversation = vk_session.method("messages.getConversationMembers",
                                         {"peer_id": event.chat_id + 2000000000, "fields": 'online'})
        return Conversation['profiles']

    # Массив для получения онлайн|оффлайн пользователей
    def online_msg(event):
        ids = []
        for i in Users.Profiles(event):
            if i['online'] == 1:
                ids += [f'[❌] | *id{str(i["id"])}({Users.User_Name_Id(event, i["id"])})']
                text = '\n'.join(map(str, ids))
        return f"""
⚙ Количество пользователь онлайн на данный момент: {len(ids)}

📎 Пользователи, которые сейчас онлайн:

{text}
                 """

    def offline_msg(event):
        ids = []
        for i in Users.Profiles(event):
            if i['online'] == 0:
                ids += [f'[❌] | *id{str(i["id"])}({Users.User_Name_Id(event, i["id"])})']
                text = '\n'.join(map(str, ids))
        return f"""
⚙ Количество пользователь оффлайн на данный момент: {len(ids)}

📎 Пользователи, которые сейчас онлайн:

{text}
                         """

    # Получаем айди создателя беседы
    def is_owner(event):
        Converasion = vk_session.method("messages.getConversationMembers",
                                        {"peer_id": event.chat_id + 2000000000, "fields": 'online'})
        members = Converasion['items']
        for i in range(len(members)):
            if members[i]["is_owner"] == True:
                try:
                    own_id = members[i]["member_id"]
                    return own_id
                except:
                    continue

# класс для работы с беседами
class Chats:
    def __init__(self, event):
        self.event = event

    # Получение названия беседы
    def Title(event):
        Converasion = vk_session.method("messages.getConversationsById",
                                        {"peer_ids": event.chat_id + 2000000000})
        info = Converasion['items'][0]['chat_settings']['title']

        return info

    # Получение полной ссылки
    def Link(self):
        link = vk.messages.getInviteLink(
            peer_id=self.event.chat_id + 2000000000,
            reset=0,
        )
        return link

    # Проверяем, добавили ли пользователя или же он попал в чат по ссылке.
    def action(event):
        try:
            chat_invite = event.object.message['action']
            if chat_invite['type'] == 'chat_invite_user':
                return True
            else:
                return False
        except:
            pass

    # Получение айди забанненого пользователя. Да, можно было эти две функции поместить в одну функцию, но лень.
    def action_id(event):
        try:
            chat_invite = event.object.message['action']
            return chat_invite['member_id']
        except:
            pass
