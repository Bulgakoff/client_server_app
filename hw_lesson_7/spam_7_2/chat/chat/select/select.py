from socket import *

HOST = ''  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 10000  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 4096  # размер буфера 1Кбайт
ADDR = (HOST, PORT)  # адрес сервера
server_socket = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
print(server_socket,'==========================')
server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_socket.bind(ADDR)  # связываем сокет с адресом
server_socket.listen()  # устанавливаем максимальное число клиентов одновременно обслуживаемых
ENCODE='utf-8'

def accept_connection(server_socket):
    while True:  # бесконечный цикл сервера
        print('Waiting for client...')
        client_socket, addr = server_socket.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет server_socket)
        print(f'Connected from: {addr[0]}')
        send_message(client_socket)
        # server_socket.close()  # закрытие со

def send_message(client_socket):
    while True:  # цикл связи
        request = client_socket.recv(BUFSIZ)  # принимает данные от клиента
        if not request:
            break  # разрываем связь если данных нет
        else:
            responce = 'Hello bro!\n'.encode(ENCODE)
            client_socket.send(responce)  # отвечаем клиенту его же данными

    client_socket.close()  # закрываем сеанс (сокет) с клиентом

if __name__ == '__main__':
    accept_connection(server_socket)

