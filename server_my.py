from contextlib import closing
from socket import *
import json
import requests
import time
import click

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
BUFSIZ = 640
ENCODE = 'utf-8'


def current_start_server(addr, port):
    lst_answers_after_auth_json = json.dumps(LIST_AUTH)
    PROBE_json = json.dumps(PROBE)

    # tcpSerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    with socket(AF_INET, SOCK_STREAM) as s_tsp: # создаем сокет сервера
        s_tsp.bind((addr, int(port)))  # связываем сокет с адресом И ПОРТОМ
        s_tsp.listen(5)  # клиентов 5
        print('Server in listening..........')

        while True:  # бесконечный цикл сервера
            print('Waiting for client...')
            # tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept()
            tcpCliSock, addr = s_tsp.accept()  # ждем клиента, при соединении .accept()
            with closing(tcpCliSock):
                print(f'Connected from: {addr[0]}')
                while True:  # цикл связи
                    data = tcpCliSock.recv(BUFSIZ)  # принимает данные от клиента
                    data_dict = json.loads(data.decode(ENCODE))
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
                        print('прилетел presence')
                    elif 'action' in data_dict and data_dict['action'] == 'quit':
                        tcpCliSock.send('finish'.encode(ENCODE))
                        print(f'прилетел quit {time.ctime()}')
                    elif 'action' in data_dict and data_dict['action'] != 'authenticate':
                        for var_response in auth_response_server_list:
                            if 'response' in var_response and var_response['response'] == 402:
                                msg = var_response['error']
                                tcpCliSock.send(bytes(msg, ENCODE))
                        print('ошибка auth')


            # tcpCliSock.close()  # закрываем сеанс (сокет) с клиентом


            # tcpSerSock.close()  # закрытие сокета сервера



# ==========click============
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_server(addr, port)


if __name__ == '__main__':
    main()
