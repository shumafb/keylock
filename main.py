import hello
import db

hello.hello()
while True:
    cmd = input('Введите одну из команд \n(Д)обавить / (П)осмотреть / (В)ыход\n'
                '(A)dd / (V)iew / (E)xit: ')
    if cmd[0].lower() == 'в' or cmd[0].lower() == 'e':
        exit()
    elif cmd[0].lower() == 'д' or cmd[0].lower() == 'a':
        db.additem(input('Введите данные для добавления: [Название] [Логин] [Пароль]: '))
    elif cmd[0].lower() == 'п' or cmd[0].lower() == 'v':
        db.asciiview()
    else:
        None
