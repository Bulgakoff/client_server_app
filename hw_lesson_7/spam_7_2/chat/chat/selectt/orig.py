import socket

HOST = ""  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 2222  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 4096  # размер буфера 1Кбайт
ENCODE = 'utf-8'
ADDR = (HOST, PORT)  # адрес сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет сервера
print(server_socket, '==========================')
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 1111))  # связываем сокет с адресом
server_socket.listen(5)

while True:
    print('Waiting for client....or..')
    client_socket, addr = server_socket.accept()
    print('Connected from: ', addr)
    while True:
        request = client_socket.recv(BUFSIZ)
        if not request:
            break  # разрываем связь если данных нет
        else:
            responce = 'Hello bro!\n'.encode()
            client_socket.send(responce)
    print('end')
    client_socket.close()

