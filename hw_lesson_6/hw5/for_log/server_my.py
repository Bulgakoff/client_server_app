import inspect
from contextlib import closing
from functools import wraps
from socket import *
import json
import requests
import time
import click
import logging
import server_log_config

times = time.ctime()
logger = logging.getLogger('app2.main')
# Ответы сервераa
LIST_AUTH = [
    {
        "response": 200,
        "alert": "An optional message/notification - Ok!"
    },
    {
        "response": 402,
        "error": "This could be 'wrong password' or 'no account with that name'"
    },
]
PROBE = {
    "action": "probe!!!",
    "time": time.time(),
}


# ========================log===================================================
def log_decorator(foo):
    @wraps(foo)
    def wrap(*args, **kwargs):  # если в функции есть параметры то нужен пропих
        stack = inspect.stack()
        res = stack[1].function
        logger.debug(f'Go function {foo.__name__} from function {res} in {times} ')
        return foo(*args, **kwargs)
    return wrap


# ========================log=============================================
# =====================server=======================================
# =====================server=======================================
HOST = ''
PORT = 1111
BUFSIZ = 2048
ENCODE = 'utf-8'

@log_decorator
def tcp_sock_create():
    return socket(AF_INET, SOCK_STREAM)

@log_decorator
def bind_create_from_user(s_tsp, addr, port):
    return s_tsp.bind((addr, int(port)))

@log_decorator
def server_listen_ready(s_tsp):
    return s_tsp.listen(5)

@log_decorator
def recved_data(user_socket):
    return user_socket.recv(BUFSIZ)

@log_decorator
def b_decode_str_foo(b_data_recvd):  # from b'' (json) to str
    return b_data_recvd.decode(ENCODE)

@log_decorator
def str_loads_dict_foo(data_str):  # from str to  dict
    return json.loads(data_str)

@log_decorator
def py_dumps_str_foo(param_server):  # from py (dict) to str
    return json.dumps(param_server)


@log_decorator
def current_start_server(addr, port):
    lst_answers_after_auth_json = py_dumps_str_foo(LIST_AUTH)
    PROBE_json = py_dumps_str_foo(PROBE)
    # tcpSerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    with tcp_sock_create() as s_tsp:  # создаем сокет сервера
        bind_create_from_user(s_tsp, addr, port)  # связываем сокет с адресом И ПОРТОМ
        logger.debug(f'======================')
        # s_tsp.listen(5)  # клиентов 5
        server_listen_ready(s_tsp)
        logger.debug('Server in listening..........')

        while True:  # бесконечный цикл сервера
            print('Waiting for client...')
            # tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept()
            tcpCliSock, addr = s_tsp.accept()  # ждем клиента, при соединении .accept()
            with closing(tcpCliSock):
                logger.debug(f'Connected from: {addr[0]}')
                while True:  # цикл связи
                    # data = tcpCliSock.recv(BUFSIZ)  # принимает данные от клиента
                    data = recved_data(tcpCliSock)
                    # data_dict = json.loads(data.decode(ENCODE))
                    data_str = b_decode_str_foo(data)
                    data_dict = str_loads_dict_foo(data_str)
                    auth_response_server_list = json.loads(lst_answers_after_auth_json)

                    if not data:
                        break  # разрываем связь если данных нет
                    if 'action' in data_dict and data_dict['action'] == 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 200:
                                msg = var_response['alert']
                                tcpCliSock.send(bytes(msg, ENCODE))

                    elif 'action' in data_dict and data_dict['action'] == 'presence':
                        msg = PROBE_json.encode(ENCODE)
                        tcpCliSock.send(msg)
                        logger.debug('прилетел presence')
                    elif 'action' in data_dict and data_dict['action'] == 'quit':
                        tcpCliSock.send('finish'.encode(ENCODE))
                        print(f'прилетел quit {time.ctime()}')
                    elif 'action' in data_dict and data_dict['action'] != 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 402:
                                msg = var_response['error']
                                tcpCliSock.send(bytes(msg, ENCODE))
                        logger.debug('ошибка auth')


# ==========click============
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_server(addr, port)
    # logging.debug('Старт current_start_server')


if __name__ == '__main__':
    main()
