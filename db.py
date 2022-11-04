import bcrypt
from crypt import generate
from tinydb import TinyDB, Query
from prettytable import PrettyTable

db = TinyDB('db.json')
Search = Query()
mpass = db.table('masterpassword')
salt = bcrypt.gensalt()


class Mpass:
    """Работа с мастер-паролем"""

    def __init__(self, mpswd):
        """Конструктор"""
        self.mpassword = mpswd

    def changempass(self):
        """Изменение мастер-пароля"""
        mpass.update({'password': str(bcrypt.hashpw(self.encode('utf-8'), salt).decode())}, Search.name == 'mpass')
        print('Мастер-пароль успешно изменен')

    def login(self):
        if bcrypt.checkpw(self.encode('utf-8'), showmpass().encode('utf-8')):
            return False
        else:
            return True
        
def showmpass():
    return list(mpass.get(Search.name == 'mpass').values())[1]

def asciiview():
    """Вывод всех эементов БД в табличном виде"""
    view = PrettyTable()
    view.field_names = ['Название', 'Логин', 'Пароль', 'Примечание']
    for i in db:
        view.add_row(list(i.values()))
    print(view)

def additem(item):
    """Принимает строку с данными и вносит новый элемент в БД"""
    item = item.split()
    if item[2][:9] == 'generate-':
        item[2] = generate(int(item[2][item[2].index('-') + 1:]))
    if len(item) == 3:
        print('Карточка добавлена')
        return db.insert({'name': item[0], 'login': item[1], 'password': item[2], 'notes': None})
    elif len(item) == 4:
        return db.insert({'name': item[0], 'login': item[1], 'password': item[2], 'notes': item[3]})
        print('Карточка добавлена')

def removeitem(item):
    """Принимает строку и удаляет элемент с подходящими входными данными"""
    while True:
        if Search.name == item:  # Не работает условие присутствия, пересмотреть код
            print('Карточка успешно удалена')
            x = db.get(Search.name == item)
            return db.remove(doc_ids=[x.doc_id])
            break
        else:
            print('Карточка отсутствует. Проверьте данные')
            break

def burndb():
    """Очищение базы данных"""
    db.truncate()
    print('База данных успешно очищена')
    asciiview()


