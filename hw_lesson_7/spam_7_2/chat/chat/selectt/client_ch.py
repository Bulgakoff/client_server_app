from socket import AF_INET, SOCK_STREAM,socket
import time
HOST = '127.0.0.1'  # локальный адрес localhost или 127.0.0.1
PORT = 1111  # порт на котором работает сервер
BUFSIZ = 4096
ADDR = (HOST, PORT)
ENCODE='utf-8'
s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(ADDR)  # Соединиться с сервером
msg = "Hi server!"
s.send(msg.encode(ENCODE))
data = s.recv(BUFSIZ) # получаем данные от сервера
print("Сообщение от сервера: ", data.decode(ENCODE),
      ", длиной ", len(data), " байт")
time.sleep(5)
s.close()
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
