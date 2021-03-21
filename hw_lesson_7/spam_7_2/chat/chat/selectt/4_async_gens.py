import select
from socket import AF_INET, SOCK_STREAM, socket

HOST = ""  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 2222  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 4096  # размер буфера 1Кбайт
ENCODE = 'utf-8'
ADDR = (HOST, PORT)  # адрес сервера

tasks = []

to_read = {}  # ключ сокет, значение - генератор
to_write = {}  # ключ сокет, значение - генератор


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет сервера
    print(server_socket, '==========================')
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 1111))  # связываем сокет с адресом
    server_socket.listen(5)
    print('Waiting for client....or..')

    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept()  # read

        print('Connected from: ', addr)
        client(client_socket)


def client(client_socket):
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(BUFSIZ)  # read

        if not request:
            break  # разрываем связь если данных нет
        else:
            responce = 'Hello bro!\n'.encode()

            yield ('wrire', client_socket)
            client_socket.send(responce)  # write

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):  # если хоть один из
        # списка TRue  any return  TRUE
        while not tasks:
            ready_to_read, ready_to_write, _ = select.select(to_read, to_write, [])


tasks.append(server())
