from m_chat.messages import *
from m_chat.serializer import Serializer
from m_chat.send_buffer import SendBuffer


class Disconnector:
    def __init__(self, send_buffer,
                 serializer=Serializer()):
        self._send_buffer = send_buffer
        self._serializer = serializer

    def disconnect(self):
        """Прерывает  работу  и отсылает quit"""
        quit_msg = AnwQuit('quit')
        data = self._serializer.serialize(quit_msg)
        self._send_buffer.send(data)

