import select
from socket import socket, AF_INET, SOCK_STREAM


def read_requests(r_clietns, all_clients_list):
    responses = {}
    for sock in r_clietns:
        try:
            message_to_send = sock.recv(1024).decode("utf-8")
            responses[sock] = message_to_send
            broadcast(message_to_send, sock, all_clients_list)
        except:
            print("Клиент {} {} отключился".format(sock.fileno()
                                                   , sock.getpeername()))
            all_clients_list.remove(sock)
        # else:

    return responses


def write_responses(requests, w_clients, all_clients):
    """ Эхо-ответ сервера клиентам, от которых были запросы
    """
    for sock in w_clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode("utf-8")
                # Эхо-ответ сделаем чуть непохожим на оригинал
                sock.send(resp.upper())
            except:  # Сокет недоступен, клиент отключился
                print(f"Клиент {sock.fileno()} {sock.getpeername()} отключился")

                sock.close()
                all_clients.remove(sock)


def broadcast(msg, socket, clients_lst):
    for client in clients_lst:
        if client != socket:
            try:
                client.send(msg)
            except:
                pass


def mainloop():
    """ Основной цикл обработки запросов клиентов
    """
    address = ("", 10000)
    clients = []

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(address)
        s.listen(5)
        s.settimeout(0.2)  # Таймаут для операций с сокетом
        while True:
            try:
                conn, addr = s.accept()  # Проверка подключений
            except OSError as e:
                pass  # timeout вышел
            else:
                print("Получен запрос на соединение от %s" % str(addr))
                clients.append(conn)
                print(f'=============={clients}')
            finally:
                # Проверить наличие событий ввода-вывода
                wait = 5
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except:
                    pass  # Ничего не делать, если какой-то клиент отключился

                # print(f'=--rr after recv---{r}')
                # print(f'=ww after send={w}')
                requests = read_requests(r, clients)  # ПРинимаем запросы клиентов
            if requests:
                write_responses(requests, w, clients)  # формируем ответ и отправляем его


print("Эхо-сервер запущен!")
mainloop()
