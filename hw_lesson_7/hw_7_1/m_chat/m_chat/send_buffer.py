import socket
import json
from m_chat.deserializer import Deserializer

# оберткa над буфером с исходящими данными
class SendBuffer:
    def __init__(self, msg_parser=None,
                 msg_handler=None,
                 deserializer=Deserializer()):
        self._out_data = b''
        self._msg_parser = msg_parser
        self._desialiser = deserializer
        self._msg_handler = msg_handler

    def send(self, data):
        self._out_data += data

    def bytes_sent(self, size):
        self._out_data = self._out_data[size:]

    def feed_data(self, data_bytes):
        parser_data_j = self._desialiser.deserialize(data_bytes)# decode = тут json_msg
        msg_data_class = self._msg_parser.parse(parser_data_j)
        self._msg_handler.on_msg(msg_data_class)
