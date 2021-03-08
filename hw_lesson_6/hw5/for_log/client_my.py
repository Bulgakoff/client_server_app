# Программа сервера для ОТПРАВКИ приветствия сервера и получения ответа
from socket import *
import json
import time
import click
import requests
import re
import logging
import client_log_config
import inspect
times=time.ctime()
logger = logging.getLogger('app.main')
# запросы клиента:
quit = {
    'action': 'quit'
}
AUTH_CLIENT = {
    'action': 'authenticate',
    # 'action': 'dfgdfg',
    'time': times,
    'user': {
        'account_name': 'C0deMaver1ck',
        'password': 'CorrectHorseBatterStaple'
    }
}
PRESENTS_MSG = {  # сообщение о присутствии — presence
    'action': 'presence',
    'time': times,
    'type': 'status',
    'user': {
        'account_name': 'C0deMaver1ck',
        'status': 'Yep, I am here!'
    }
}


# ========================client===================================================

# ========================client===================================================
# ========================log===================================================
def log_decorator(foo):
    def wrap(*args, **kwargs):  # если в функции есть параметры то нужен пропих
        res = foo(*args, **kwargs)
        logger.debug(f'Go function {foo.__name__} from function {res} in {times} ')

    return wrap

# def log_decr(foo):
#     def wrap(*args, **kwargs):  # если в функции есть параметры то нужен пропих
#         foo(*args, **kwargs)
#         logger.debug(f'Go function {foo.__name__} from function  in {times} ')
#
#     return wrap

# ========================log===================================================
#
BUFSIZ = 640
ENCODE = 'utf-8'

# @log_decr
def py_dumps_str_foo(param_user):
    stack = inspect.stack()
    print(stack[1].function)
    return json.dumps(param_user)


def tcp_sock_create():
    return socket(AF_INET, SOCK_STREAM)


@log_decorator
def current_start_client(addr, port):
    stack = inspect.stack()
    res = stack[5].function
    print(res)
    # auth_from_client_json = json.dumps(AUTH_CLIENT)
    auth_from_client_json = py_dumps_str_foo(AUTH_CLIENT)
    # logger.debug('Старт py_dumps_str_foo')
    msg_presence_json = py_dumps_str_foo(PRESENTS_MSG)
    # logger.debug('Старт py_dumps_str_foo')
    quit_json = py_dumps_str_foo(quit)
    # logger.debug('Старт py_dumps_str_foo')

    # tcpCliSock = socket(AF_INET, SOCK_STREAM)
    with tcp_sock_create() as tcpCliSock:
        logger.debug('Старт tcp_sock_create')
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

    return res
# ==========click============

@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_client(addr, port)


if __name__ == '__main__':
    main()
