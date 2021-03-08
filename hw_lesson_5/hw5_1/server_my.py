from contextlib import closing
from socket import *
import json
import requests
import time
import click
import logging

# from sserver_log import setup_logging
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)s---%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('log_dir/ser.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

logger=setup_logging()

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

# =====================server=======================================
# =====================server=======================================
HOST = ''
PORT = 1111
BUFSIZ = 2048
ENCODE = 'utf-8'


def tcp_sock_create():
    return socket(AF_INET, SOCK_STREAM)


def bind_create_from_user(s_tsp, addr, port):
    return s_tsp.bind((addr, int(port)))


def server_listen_ready(s_tsp):
    return s_tsp.listen(5)


def recved_data(user_socket):
    return user_socket.recv(BUFSIZ)


def b_decode_str_foo(b_data_recvd):  # from b'' (json) to str
    return b_data_recvd.decode(ENCODE)


def str_loads_dict_foo(data_str):  # from str to  dict
    return json.loads(data_str)


def py_dumps_str_foo(param_server):  # from py (dict) to str
    return json.dumps(param_server)


def current_start_server(addr, port):
    lst_answers_after_auth_json = py_dumps_str_foo(LIST_AUTH)
    PROBE_json = py_dumps_str_foo(PROBE)
    # tcpSerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    with tcp_sock_create() as s_tsp:  # создаем сокет сервера
        logging.debug('tcp_sock_create!!!!!!!!!!!!!!!')
        bind_create_from_user(s_tsp, addr, port)  # связываем сокет с адресом И ПОРТОМ
        logging.debug(f'======================')
        # s_tsp.listen(5)  # клиентов 5
        server_listen_ready(s_tsp)
        logging.debug('Server in listening..........')

        while True:  # бесконечный цикл сервера
            logging.debug('Waiting for client...')
            # tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept()
            tcpCliSock, addr = s_tsp.accept()  # ждем клиента, при соединении .accept()
            with closing(tcpCliSock):
                logging.debug(f'Connected from: {addr[0]}')
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
                        logging.debug('прилетел presence')
                    elif 'action' in data_dict and data_dict['action'] == 'quit':
                        tcpCliSock.send('finish'.encode(ENCODE))
                        logging.debug(f'прилетел quit {time.ctime()}')
                    elif 'action' in data_dict and data_dict['action'] != 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 402:
                                msg = var_response['error']
                                tcpCliSock.send(bytes(msg, ENCODE))
                        logging.debug('ошибка auth')


# ==========click============
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_server(addr, port)


# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s ",
#     filename='qwe.log'
# )
if __name__ == '__main__':
    logger.debug('START server!!!!!!!!!!!!!!!')
    main()
