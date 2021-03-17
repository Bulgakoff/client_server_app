import sys
from socket import *
import json
import time

ADDRESS = ("localhost", 10000)


def echo_client():
    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет авторматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        sock.connect(ADDRESS)  # Соединиться с сервером
        while True:
            msg_py = {"action": "authenticate",
                      "time": 123,
                      "user": {
                          "account_name": "C0deMaver1ck",
                          "password": "CorrectHorseBatterStaple"
                      }
                      }
            # join_chat = {"action": "join",
            #              "time": time.ctime(),
            #              "room": "#room_name"}
            msg_str = json.dumps(msg_py)
            sock.send(msg_str.encode("utf-8"))  # Отправить!
            time.sleep(2)
            data = sock.recv(1024).decode("utf-8")
            print("Ответ:", data)


if __name__ == "__main__":
    echo_client()
