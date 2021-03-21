import json
from m_chat.deserializer import Deserializer
from m_chat.msg_parser import MsgParser
from m_chat.messages_handler import MessageHandler

class MessageSplitter:
    """Разделитель для входящих сообщений"""

    def __init__(
            self,
            msg_handler,
            deserializer=Deserializer(),
            msg_parser=MsgParser(),

    ):
        self._data_recv = b'',
        self._msg_handler = msg_handler
        self._desialiser = deserializer
        self._msg_parser_py = msg_parser


    def feed_data(self, data_bytes):  # recv(...)
        """для входящих сообщений"""
        self._data_recv += data_bytes
        parser_data_py = self._desialiser.deserialize(data_bytes)  # loads => тут dict_msg
        msg_data_class = self._msg_parser_py.parse(parser_data_py) # => dataclass
        self._msg_handler.on_msg(msg_data_class)