# Программа сервера для ПОЛУЧЕНИЯ приветствия от клиента и отправки ответа
# Команды запуска:
# python my_server.py -a 127.0.0.1 -p 8888
# python my_client.py -a 127.0.0.1 -p 8888
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
probe_server_response = {
    "action": "probe!!!",
    "time": time.time(),
}


# =====================server=======================================
# click
def current_start_server(addr, port):
    lst_answers_after_auth_json = json.dumps(LIST_AUTH)
    probe_server_response_json = json.dumps(probe_server_response)

    with socket(AF_INET, SOCK_STREAM) as s:  # Создает сокет TCP
        s.bind((addr, int(port)))  # Присваивает порт 8888 (только по данному порту)
        s.listen()  # просигнализировать о готовности принимать соединения


        while True:
            client, addr = s.accept()  # принять запрос на установку соединения
            with closing(client) as cl:  # затем закрываем сокет клиента
                data = cl.recv(640)  # принимает сервер "Hi server!" от клиента
                data_dict = json.loads(data.decode("utf-8"))
                auth_response_server_list = json.loads(lst_answers_after_auth_json)
                if data_dict['action'] == 'authenticate':
                    for var_response in auth_response_server_list:
                        if var_response['response'] == 200:
                            msg = var_response['alert']
                            cl.send(bytes(msg, 'utf-8'))
                else:
                    msg = auth_response_server_list[1]['error']
                    cl.send(bytes(msg, 'utf-8'))

                if data_dict['action']=="presence":
                    msg = data_dict['action']
                    cl.send(bytes(msg, 'utf-8'))


                print(
                    "Сообщение: ", "action == ", data_dict['action'],
                    type(data.decode("utf-8")), type(auth_response_server_list),
                    ", было отправлено клиентом: "
                )


@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_server(addr, port)


if __name__ == '__main__':
    main()
