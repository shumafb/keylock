from tinydb import TinyDB, Query
from prettytable import PrettyTable

db = TinyDB('db.json')
view = PrettyTable()

def asciiview():
    view.field_names = ['Название', 'Логин', 'Пароль', 'Примечание']
    for i in db:
        view.add_row(list(i.values()))
    print(view)

def additem(item):
    Search = Query()
    item = item.split()
    while True:
        x = input('Хотите добавить заметку? [(Д)а/(Н)ет] ')
        if x[0].lower() == 'д':
            notes = input('Введите заметку: ')
            break
        elif x[0].lower() == 'н':
            notes = None
            break
        else:
            print('Введите одну из команд')
    db.update({'notes': notes}, Search.name == item[0])
    return db.insert({'name': item[0], 'login': item[1], 'password': item[2], 'notes': notes})

