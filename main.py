import welcome
import db
from db import Mpass

welcome.hello()
while True:
    cmd = input('\nВведите одну из команд \n(Д)обавить / (У)далить / (П)осмотреть / [См]енить мастер-пароль / (В)ыход /\n'
                '(A)dd / (R)emove / (V)iew / [Ch]ange masterpassword (E)xit: ')
    if cmd == '':
        continue
    elif cmd[0].lower() == 'в' or cmd[0].lower() == 'e':
        print('Выход из программы')
        exit()
    elif cmd[0].lower() == 'д' or cmd[0].lower() == 'a':
        while True:
            x = input('Введите данные для добавления:'
                      ' [Название] [Логин] [Пароль] или (В)ыход / (E)xit для выхода в меню: ')
            if x == '':
                continue
            elif x[0].lower() == 'в' or x[0].lower() == 'e':
                break
            elif len(x.split()) == 3 or len(x.split()) > 3:
                db.additem(x)
                break
            elif len(x.split()) < 3:
                print('Введите элементы карточки')
                continue
    elif cmd[0].lower() == 'п' or cmd[0].lower() == 'v':
        db.asciiview()
    elif cmd[0].lower() == 'у' or cmd[0].lower() == 'r':
        while True:
            x = input('Введите [Название] или (В)ыход / (E)xit для выхода в меню: ')
            if x == '':
                continue
            elif x[0].lower() == 'в' or x[0].lower() == 'e':
                break
            elif len(x.split()) == 1:
                db.removeitem(x)
                break
            else:
                print('Введите [Название] карточки\n')
                continue
    elif cmd[:2].lower() == 'см' or cmd[:2].lower() == 'ch':
        while True:
            x = input('Введите старый мастер-пароль или (В)ыход / (E)xit для выхода в меню: ')
            if x == '':
                continue
            elif x[0].lower() == 'в' or x[0].lower() == 'e':
                break
            elif x == db.showmpass():
                Mpass.changempass(input('Введите новый пароль: '))
                break
            else:
                print('Неправильно введен мастер-пароль')
                continue
    else:
        None
