import json
from Parser import *
import time
from datetime import datetime
from TrojanCommands.message import message


class JS:
    # Очень долго тут все описывать, суть в том, что сервер слабый, поэтому вместо базы данных используется Json. Все функции в данном классе работают лишь с ним и ивентом вк.
    # Если у вас хороший сервер,
    # То рекомендую пользоваться MYSQL, особенно для таких маленьких проектов)

    def __init__(self, text, v, v1, name, name_1, value, check_value, Base):
        self.text = text
        self.v = v
        self.v1 = v1
        self.name = name
        self.name_1 = name_1
        self.value = value
        self.check_value = check_value
        self.Base = Base

    # Данная функция работает с файлами Json, считайте, что Json файлы эквивалент базы данных, но в отличии от них он менее требовалетен и очень тягуч.
    def Value_v(text, v1, name, Base):
        # data - переменная, в которой теперь хранится наш json файл.
        data = json.load(open(Base))
        jsid = text
        # jsid - переменная, в которой мы
        if list(filter(lambda x: x[text] == jsid, data)):
            for i in range(len(data)):
                if data[i][text] == jsid:
                    with open(Base, 'r+') as f:
                        DisValue = data[i][name][0][v1]
                        return DisValue

    def Value(text, count, v, Base):
        # data - переменная, в которой теперь хранится наш json файл. open - открываем файл, load - загружаем.
        # text - переменная в json файле. В ней должно быть число/строка равная count
        # Base - текстовый файл, с которым мы работаем. В Pycharm это будет выглядеть: json.load(open('Error.Base))
        data = json.load(open(Base))
        jsid = count
        if list(filter(lambda x: x[text] == jsid, data)):
            for i in range(len(data)):
                if data[i][text] == jsid:
                    with open(Base, 'r+') as f:
                        Value = data[i][v]
                        All = Value
                        return All

    def New_Value(value, check_value, name, text, Base):
        data = json.load(open(Base))
        value_1 = value
        if list(filter(lambda x: x[value_1] == check_value, data)):
            for i in range(len(data)):
                if data[i][value_1] == check_value:
                    with open(Base, 'r+') as f:
                        data = json.load(f)
                        data[i][name] += text
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()

    def New_Value_List(value, check_value, name, text, Base):
        data = json.load(open(Base))
        value_1 = value
        if list(filter(lambda x: x[value_1] == check_value, data)):
            for i in range(len(data)):
                if data[i][value_1] == check_value:
                    with open(Base, 'r+') as f:
                        data = json.load(f)
                        data[i][name] += [text]
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()

    def Add_Value(value, check_value, name, text, Base):
        data = json.load(open(Base))
        value_1 = value
        if list(filter(lambda x: x[check_value] == value_1, data)):
            for i in range(len(data)):
                if data[i][check_value] == value_1:
                    with open(Base, 'r+') as f:
                        data = json.load(f)
                        data[i][name] = text
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()

    def New_Value_Before(value, check_value, name, name_1, text, Base):
        data = json.load(open(Base))
        value_1 = value
        if list(filter(lambda x: x[value_1] == check_value, data)):
            for i in range(len(data)):
                if data[i][value_1] == check_value:
                    with open(Base, 'r+') as f:
                        data = json.load(f)
                        data[i][name][0][name_1] += text
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()

    def Add_Value_Before(value, check_value, name, name_1, text, Base):
        data = json.load(open(Base))
        value_1 = value
        if list(filter(lambda x: x[value_1] == check_value, data)):
            for i in range(len(data)):
                if data[i][value_1] == check_value:
                    with open(Base, 'r+') as f:
                        data = json.load(f)
                        data[i][name][0][name_1] = text
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()

    # Проверяем, есть ли пользователь с таким айди в списке или нет.
    def chelk(v, id):
        if id in JS.Value("id", 1, v, "Values.Base"):
            return True
        else:
            return False

    def last_value(Base, V):
        data = json.load(open(Base))
        with open(Base, 'r+') as f:
            Value = data[-1][V]
            return Value

    def Prof_Creat(event, user):
        if JS.chelk("users", user) == False:
            json_data = {
                "то что мы вставляем в json файл"
            }
            data = json.load(open("Файл"))
            data.append(json_data)
            with open("Файл", "w") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            message.msg(None, event.chat_id + 2000000000, '⚙Пользователь получает ачивку!', None, None, None)
            JS.New_Value_List()

        else:
            pass

