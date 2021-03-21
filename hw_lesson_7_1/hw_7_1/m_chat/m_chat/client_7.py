#  Программа клиента, отправляющего/читающего простые текстовые сообщения на сервер

import sys
import time
from socket import *
import json
from m_chat.disconnector import Disconnector
from m_chat.messages_handler import MessageHandler
from m_chat.serializer import Serializer
from m_chat.message_processor import MessageProcessor
from m_chat.send_buffer import SendBuffer
from m_chat.message_splitter import MessageSplitter

ADDRESS = ("localhost", 10000)


def echo_client():
    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет авторматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
        sock.connect(ADDRESS)  # Соединиться с сервером

        send_buffer = SendBuffer()
        disconnector = Disconnector(send_buffer)
        msg_processor = MessageProcessor(send_buffer, disconnector)
        msg_receiver = MessageHandler(msg_processor)
        MessageSplitter(msg_receiver)

    while True:
        msg_py = {"action": "authenticate",
                  "time": 123,
                  "user": {
                      "account_name": "C0deMaver1ck",
                      "password": "CorrectHorseBatterStaple"
                  }
                  }
        msg_str = json.dumps(msg_py)
        sock.send(msg_str.encode("utf-8"))  # Отправить!
        time.sleep(2)
        data = sock.recv(1024).decode("utf-8")
        print("Ответ:", data)


if __name__ == "__main__":
    echo_client()
