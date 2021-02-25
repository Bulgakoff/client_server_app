# Программа сервера для ОТПРАВКИ приветствия сервера и получения ответа
from socket import *
import json
import time
import click
import requests
import re

# запросы клиента:
quit = {
    "action": "quit"
}
AUTH_CLIENT = {
    "action": "authenticate",
    # "action": "qweqwe",
    "time": time.ctime(),
    "user": {
        "account_name": "C0deMaver1ck",
        "password": "CorrectHorseBatterStaple"
    }
}
PRESENTS_MSG = {  # сообщение о присутствии — presence
    "action": "presence",
    "time": time.time(),
    "type": "status",
    "user": {
        "account_name": "C0deMaver1ck",
        "status": "Yep, I am here!"
    }
}


# ========================client===================================================
def current_start_client(addr, port):
    auth_from_client_json = json.dumps(AUTH_CLIENT)
    msg_presence_json = json.dumps(PRESENTS_MSG)
    quit_json = json.dumps(quit)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, int(port)))
    s.send(auth_from_client_json.encode("utf-8"))
    data = s.recv(640)
    print("Сообщение от сервера: ",data.decode('utf-8'),
          ", длиной ", len(data), " байт", "отправлено ",time.ctime())
    s.close()
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_client(addr, port)


if __name__ == '__main__':
    main()
