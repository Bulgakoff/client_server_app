# Программа сервера для ОТПРАВКИ приветствия сервера и получения ответа
from socket import *
import json
import time
import click
import requests
import re

# запросы клиента:
quit = {
    'action': 'quit'
}
AUTH_CLIENT = {
    'action': 'authenticate',
    # 'action': 'dfgdfg',
    'time': time.ctime(),
    'user': {
        'account_name': 'C0deMaver1ck',
        'password': 'CorrectHorseBatterStaple'
    }
}
PRESENTS_MSG = {  # сообщение о присутствии — presence
    'action': 'presence',
    'time': time.ctime(),
    'type': 'status',
    'user': {
        'account_name': 'C0deMaver1ck',
        'status': 'Yep, I am here!'
    }
}

# ========================client===================================================

# ========================client===================================================
BUFSIZ = 640
ENCODE = 'utf-8'


def current_start_client(addr, port):
    auth_from_client_json = json.dumps(AUTH_CLIENT)
    msg_presence_json = json.dumps(PRESENTS_MSG)
    quit_json = json.dumps(quit)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect((addr, int(port)))  # установка связи с сервером
    while True:
        time.sleep(3)
        tcpCliSock.send(auth_from_client_json.encode(ENCODE))
        # print(f'Recieved auth ')
        data = tcpCliSock.recv(BUFSIZ)  # ожидание (получение) ответа

        if data.decode(ENCODE) == 'An optional message/notification - Ok!':
            tcpCliSock.send(msg_presence_json.encode(ENCODE))
            print(data.decode(ENCODE))

        if data.decode(ENCODE) != 'spam':
            qwes = data.decode(ENCODE)
            match = re.findall(r'wrong', qwes)
            if match:
                print('authentication denied\n')
                print(data.decode(ENCODE))
                break

        if data.decode(ENCODE) != 'spam':
            qwe = data.decode(ENCODE)
            match = re.findall(r'probe!!!', qwe)
            if match:
                print('probe!!!')
                tcpCliSock.send(quit_json.encode(ENCODE))
                break






    tcpCliSock.close()


# msg_full = ''
# while True:
#     msg_from_server = s.recv(5)
#     if len(msg_from_server) <= 0:
#         break
#     msg_full += msg_from_server.decode('utf-8')
#     print(f'Текущее время: {msg_from_server.decode('utf-8')}')
#     # print( msg_from_server.decode('utf-8'))
# print(msg_full)
#
# s.close()


# ==========click============

@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_client(addr, port)


if __name__ == '__main__':
    main()
