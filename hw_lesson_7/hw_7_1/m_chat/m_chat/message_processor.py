from m_chat.serializer import Serializer
from m_chat.messages import *
from m_chat.disconnector import Disconnector


class MessageProcessor:
    def __init__(self,
                 send_buffer,
                 disconnector,
                 serializer=Serializer()
                 ):
        self._serializer = serializer
        self._send_buffer = send_buffer
        self._disconnector = disconnector

    def on_auth_response(self, msg_data_class):
        """вызывать сериалайзер для превращения сообщения в байты,
         а потом передавать эти байты в  SendBuffer """
        if msg_data_class.response != "200":
            self._disconnector.disconnect()
        else:
            presence = Presence('Bob', '"Yep, I am here!"')
            data = self._serializer.serialize(presence)
            self._send_buffer.send(data)


S
