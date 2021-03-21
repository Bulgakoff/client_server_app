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
    def on_auth(self, msg_data_class):
        # добавляем в список клиентов
        if msg_data_class.action  != "authenticate":
            response_err = ResponceError('402','epic fail')
            data = self._serializer.serialize(response_err)
            self._send_buffer.send(data)
        else:
            responce_ok = Responce('200','okok')
            data = self._serializer.serialize(responce_ok)
            self._send_buffer.send(data)
            # как выглядит добавление в список клиентов?







