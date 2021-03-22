from socket import AF_INET, SOCK_STREAM, socket
import time
import json

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

HOST = '127.0.0.1'  # локальный адрес localhost или 127.0.0.1
PORT = 1111  # порт на котором работает сервер
BUFSIZ = 4096
ADDR = (HOST, PORT)
ENCODE = 'utf-8'
with socket(AF_INET, SOCK_STREAM) as s:  # Создать сокет TCP
    s.connect(ADDR)  # Соединиться с сервером
    while True:
        msg = json.dumps(AUTH_CLIENT)
        s.send(msg.encode(ENCODE))
        data = s.recv(BUFSIZ)  # получаем данные от сервера
        print("Сообщение от сервера: ", data.decode(ENCODE),
              ", длиной ", len(data), " байт")
        time.sleep(5)
# client_sock = socket(AF_INET, SOCK_STREAM)
# # client_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# client_sock.connect(ADDR)  # установка связи с сервером
# while True:
#     data = input('>')  # ввод данных для отправки
#     if not data:
#         break
#     client_sock.send(data.encode())  # отправка данных в bytes
#     data = client_sock.recv(BUFSIZ)  # ожидание (получение) ответа
#     if not data:
#         break
#     print(data.decode(ENCODE))
# client_sock.close()
