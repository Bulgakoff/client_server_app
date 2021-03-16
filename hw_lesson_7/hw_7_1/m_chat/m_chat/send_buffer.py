import socket
import json


# для исходящих сообщений
class SendBuffer:
    """оберткa над буфером с исходящими данными"""

    def __init__(self):
        self._out_data = b''
        self._should_close = False

    @property
    def data_out(self):
        return self._out_data

    def send(self, data):
        self._out_data += data

    def bytes_sent(self, size):
        self._out_data = self._out_data[size:]

    def close(self):
        self._should_close = True
