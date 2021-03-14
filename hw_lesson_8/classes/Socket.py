import socket


class SocketCLass(socket.socket):
    def __init__(self):
        super(SocketCLass, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.BUFF = 2048
        self.ENCODDING = 'utf-8'
        self.PORT = 1111
        self.LOCAL = 'localhost'

    def send_data(self, data):
        raise NotImplementedError

    def listen_socket(self,listened_sock=None):
        raise NotImplementedError

    def set_up(self):
        raise NotImplementedError