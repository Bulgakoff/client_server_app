import select
from socket import AF_INET, SOCK_STREAM, socket
import json
import  time

def disconnect_client(sock, all_clients):
    print(f"Клиент {sock.fileno()} {sock.getpeername()} отключился")
    sock.close()
    all_clients.remove(sock)


def read_requests(r_clients, all_clients):
    responses = {}  # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:
        try:
            data_str = sock.recv(1024).decode("utf-8")
            responses[sock] = data_str

        except:
            disconnect_client(sock, all_clients)

    return responses


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        for recv_sock, data in requests.items():
            if sock is recv_sock:
                continue
            try:
                data_py = json.loads(data)
                if data_py['action']=="msg":
                    msgs_for_back = data_py['message']
                    responce = msgs_for_back.encode("ascii")
                    time.sleep(2)
                    sock.send(responce)
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
                print(f"Получен запрос на соединение от {addr}")
                clients.append(conn)
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
            sock.close()
        s.close()


print("Эхо-сервер запущен!")
mainloop()
