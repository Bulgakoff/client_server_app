import select
from socket import AF_INET, SOCK_STREAM, socket
import selectors


selector = selectors.DefaultSelector()

HOST = ''  # локальный адрес localhost или 127.0.0.1
PORT = 1111  # порт на котором работает сервер
BUFSIZ = 4096
ADDR = (HOST, PORT)
ENCODE = 'utf-8'
def server():
    server_socket = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
    print(server_socket, '==========================')
    server_socket.bind(ADDR)  # связываем сокет с адресом
    server_socket.listen()  # устанавливаем максимальное число клиентов одновременно обслуживаемых

    selector.register(fileobj=server_socket,events=selectors.EVENT_READ,data=accept_connection)



def accept_connection(server_socket):
    print('Waiting for client...')
    client_socket, addr = server_socket.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет server_socket)
    print('Connected from: ', addr)

    selector.register(fileobj=client_socket,events=selectors.EVENT_WRITE,data=send_message)




def send_message(client_socket):
    request = client_socket.recv(BUFSIZ)  # принимает данные от клиента
    if request:
        responce = 'Hello bro!\n'.encode(ENCODE)
        client_socket.send(responce)  # отвечаем клиенту его же данными
    else:
        selector.unregister(client_socket) # снялис регистрации перед закрытием сокета
        client_socket.close()  # закрываем сеанс (сокет) с клиентом


def event_loop():
    while True:
        events = selector.select()# (key,events )
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
