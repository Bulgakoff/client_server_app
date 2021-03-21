import select
from socket import AF_INET, SOCK_STREAM, socket

HOST = ''  # локальный адрес localhost или 127.0.0.1
PORT = 1111  # порт на котором работает сервер
BUFSIZ = 4096
ADDR = (HOST, PORT)
ENCODE='utf-8'

server_socket = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
print(server_socket, '==========================')
server_socket.bind(ADDR)  # связываем сокет с адресом
server_socket.listen()  # устанавливаем максимальное число клиентов одновременно обслуживаемых

to_monitor = []


def accept_connection(server_socket):
    # while True:  # бесконечный цикл сервера
    print('Waiting for client...')
    client_socket, addr = server_socket.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет server_socket)
    print('Connected from: ', addr)

    to_monitor.append(client_socket)
    # send_message(client_socket)
    # server_socket.close()  # закрытие сокета сервера


def send_message(client_socket):
    # while True:  # цикл связи
    request = client_socket.recv(BUFSIZ)  # принимает данные от клиента
    if  request:
        responce = 'Hello bro!\n'.encode(ENCODE)
        client_socket.send(responce)  # отвечаем клиенту его же данными
    else:
        client_socket.close()  # закрываем сеанс (сокет) с клиентом




def event_loop():
    while True:
        ready_to_read, _, _ = select.select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
