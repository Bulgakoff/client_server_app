import socket
import json


# оберткa над буфером с исходящими данными
class SendBuffer:
    def __init__(self, msg_handler=None):
        self._out_data = b''
        self._msg_handler = msg_handler

    def send(self, data):
        self._out_data += data

    def bytes_sent(self, size):
        self._out_data = self._out_data[size:]

#
