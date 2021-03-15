import json
from m_chat.deserializer import Deserializer
from m_chat.msg_parser import MsgParser


class MessageSplitter:
    """Разделитель для входящих сообщений"""

    def __init__(
            self, msg_handler=None,
            deserializer=Deserializer(),
            msg_parser=MsgParser(),
    ):
        self._data_recv = b'',
        self._msg_handler = msg_handler
        self._desialiser = deserializer
        self._msg_parser_py = msg_parser

    # def feed_data(self, data):
    #     # вызывается из соответствующего колбэка
    #     self._data += data
    #     msg_data_class = ...  # тут поиск и отделение отдельного сообщения
    #     self._msg_deserializer.on_message(msg_data) 
    #     self._msg_handler.on_msg(msg_data_class) \\\\\\\

    def feed_data(self, data_bytes):  # recv(...)
        self._data_recv += data_bytes
        parser_data_j = self._desialiser.deserialize(data_bytes)  # decode = тут json_msg
        msg_data_class = self._msg_parser_py.parse(parser_data_j)
        self._msg_handler.on_msg(msg_data_class)
