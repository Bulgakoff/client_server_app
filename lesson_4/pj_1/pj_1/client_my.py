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


def py_dumps_str_foo(param_user):
    return json.dumps(param_user)

def tcp_sock_create():
    return socket(AF_INET, SOCK_STREAM)

def current_start_client(addr, port):
    # auth_from_client_json = json.dumps(AUTH_CLIENT)
    auth_from_client_json = py_dumps_str_foo(AUTH_CLIENT)
    msg_presence_json = py_dumps_str_foo(PRESENTS_MSG)
    quit_json = py_dumps_str_foo(quit)

    # tcpCliSock = socket(AF_INET, SOCK_STREAM)
    with tcp_sock_create() as tcpCliSock:
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
                egg = data.decode(ENCODE)
                match = re.findall(r'wrong', egg)
                if match:
                    print('authentication denied\n')
                    time.sleep(4)
                    print(data.decode(ENCODE))
                    break

            if data.decode(ENCODE) != 'spam':
                egg = data.decode(ENCODE)
                match = re.findall(r'probe!!!', egg)
                if match:
                    print('probe!!!')
                    tcpCliSock.send(quit_json.encode(ENCODE))
                    time.sleep(3)
                    break


# ==========click============

# @click.command()
# @click.argument('addr')
# @click.argument('port')
# def main(addr, port):
#     current_start_client(addr, port)
#
#
# if __name__ == '__main__':
#     main()
