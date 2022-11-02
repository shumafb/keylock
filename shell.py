import db
import crypt
from db import Mpass

def shell():
    while True:
        cmd = input('\nВведите одну из команд:'
                    '\n(Д)обавить / (У)далить / (П)осмотреть / (Г)енератор пароля'
                    ' / [См]енить мастер-пароль / (О)чистить БД / (В)ыход\n'
                    '(A)dd / (R)emove / (V)iew / (G)enerate password'
                    ' / [Ch]ange masterpassword / (B)urn DB / (E)xit: ')
        if cmd == '':
            continue
        elif cmd[0].lower() == 'в' or cmd[0].lower() == 'e':
            print('Выход из программы')
            exit()
        elif cmd[0].lower() == 'д' or cmd[0].lower() == 'a':
            while True:
                x = input('Введите данные для добавления '
                          '[Название] [Логин] [Пароль или generate-[количество символов]]\n'
                          'или (В)ыход / (E)xit: ')
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
                x = input('Введите [Название] или (В)ыход / (E)xit: ')
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
                x = input('Введите старый мастер-пароль или (В)ыход / (E)xit: ')
                if x == '':
                    continue
                elif x[0].lower() == 'в' or x[0].lower() == 'e':
                    break
                elif db.Mpass.login(x) is False:
                    Mpass.changempass(input('Введите новый пароль: '))
                    break
                else:
                    print('Неправильно введен мастер-пароль')
                    continue
        elif cmd[0].lower() == 'г' or cmd[0].lower() == 'g':
            print(crypt.generate(int(input('Введите количество символов: '))))
        elif cmd[0].lower() == 'о' or cmd[0].lower() == 'b':
            while True:
                x = input('Введите мастер-пароль для подтверждения или (В)ыход / (E)xit: ')
                if x == '':
                    continue
                elif x[0].lower() == 'в' or x[0].lower() == 'e':
                    break
                elif db.Mpass.login(x) == False:
                    db.burndb()
                    break
                else:
                    print('Неправильно введен мастер-пароль')
                    continue
        else:
            None
