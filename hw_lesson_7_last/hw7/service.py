from  subprocess import Popen,CREATE_NEW_CONSOLE
import os

p_list = []
while True:
    user = input("Запустить 10 клиентов (s) "
                 "/ Закрыть клиентов (x) /"
                 " Выйти (q) ")

    if user == 'q':
        break
    elif user == 's':
        for _ in range(5):
            p_list.append(Popen('python qwec.py',
                                 creationflags=CREATE_NEW_CONSOLE))
        print(' Запущено 10 клиентов')
    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()