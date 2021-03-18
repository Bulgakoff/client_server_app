import select
from socket import AF_INET, SOCK_STREAM, socket

from m_chat.disconnector import Disconnector
from m_chat.message_processor import MessageProcessor
from m_chat.messages_handler import MessageHandler
from m_chat.send_buffer import SendBuffer
from m_chat.message_splitter import MessageSplitter


def disconnect_client(sock, all_clients):
    print(f"Клиент {sock.fileno()} {sock.getpeername()} отключился")
    sock.close()
    all_clients.remove(sock)


def read_requests(r_clients, all_clients):
    responses = {}  # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            # data = sock.recv(1024)
            # responses[sock] = data
            # responses[sock].feed_data(data)
            data = sock.recv(1024)
            _, msg_splitter = all_clients[sock]
            msg_splitter.feed_data(data)

        except:
            disconnect_client(sock, all_clients)

    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        try:
            # sent_size = sock.send(all_clients[sock]._out_data)
            # all_clients[sock].bytes_sent(sent_size)
            send_buffer, _ = all_clients[sock]
            sent_size = sock.send(send_buffer._out_data)
            send_buffer.bytes_sent(sent_size)
        except:  # Сокет недоступен, клиент отключился
            disconnect_client(sock, all_clients)


def mainloop():
    address = ("", 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(address)
        s.listen(5)
        s.settimeout(0.2)  # Таймаут для операций с сокетом
        while True:
            try:
                conn, addr = s.accept()  # Проверка подключений
            except OSError:
                pass  # timeout вышел
            else:
                # print(f"Получен запрос на соединение от {addr}")
                # clients.append(conn)
                msg_reciever = MessageHandler(MessageProcessor(SendBuffer(),
                                                               Disconnector(SendBuffer())
                                                               ))
                clients[conn] = (SendBuffer(), MessageSplitter(msg_reciever))
            finally:
                # Проверить наличие событий ввода-вывода
                wait = 5
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except:
                    pass  # Ничего не делать, если какой-то клиент отключился

                requests = read_requests(r, clients)  # Сохраним запросы клиентов
                write_responses(
                    requests, w, clients
                )  # Выполним отправку ответов клиентам
    finally:
        for sock in clients:
            sock.close()  # ?????????????????????
        s.close()


print("Эхо-сервер запущен!")
mainloop()
