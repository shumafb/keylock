import db
from db import Mpass
def hello():
    """Вызов вступительной заставки"""
    print(" _                  _               _\n"
          "| | __  ___  _   _ | |  ___    ___ | | __\n"
          "| |/ / / _ \| | | || | / _ \  / __|| |/ /\n"
          "|   < |  __/| |_| || || (_) || (__ |   <\n"
          "|_|\_\ \___| \__, ||_| \___/  \___||_|\_\ \n"
          "             |___/                       ")
    print('Добро пожаловать в keylock')

    flag = True
    while flag:
        if list(db.mpass.get(db.Search.name == 'mpass').values())[1] == None:
            Mpass.changempass(input('Задайте мастер-пароль: '))
        else:
            flag = Mpass.login(input('Введите мастер-пароль для входа: '))

