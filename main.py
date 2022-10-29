import welcome
import db

welcome.hello()
while True:
    cmd = input('\nВведите одну из команд \n(Д)обавить / (У)далить / (П)осмотреть / (В)ыход\n'
                '(A)dd / (R)emove / (V)iew / (E)xit: ')
    if cmd[0].lower() == 'в' or cmd[0].lower() == 'e':
        exit()
    elif cmd[0].lower() == 'д' or cmd[0].lower() == 'a':
        db.additem(input('Введите данные для добавления: [Название] [Логин] [Пароль]: '))
    elif cmd[0].lower() == 'п' or cmd[0].lower() == 'v':
        db.asciiview()
    elif cmd[0].lower() == 'у' or cmd[0].lower() == 'r':
        db.removeitem(input('Введите [Название]: '))
    else:
        None
