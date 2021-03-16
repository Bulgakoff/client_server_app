from m_chat.messages \
    import Authenticate, AnwClient, AnwQuit

from m_chat.serializer \
    import Serializer

from m_chat.deserializer \
    import Deserializer


class Client:
    def __init__(self, client_socket,
                 account_name,
                 serializer=Serializer()):
                 # deserializer=Deserializer()):
        self._client_socket = client_socket
        self._account_name = account_name
        self._serializer = serializer
        # self._deserializer = deserializer

    def on_auth_response(self, msg_data_class):
       pass

    # def authenticate(self, password):
    #     obj_A_msg = Authenticate(self._account_name,
    #                              password)
    #     data_byte = self._serializer.serialize(obj_A_msg)
    #     self._client_socket.send(data_byte)
    #
    # def presence(self, status):
    #     obj_A_msg = AnwClient(self._account_name, status)
    #     data_byte = self._serializer.serialize(obj_A_msg)
    #     self._client_socket.send(data_byte)
    #
    # def cl_get_ok_response_after_auth(self):
    #     pass
    # def cl_get_ok_response_after_auth(self):
    #     data_b = self._client_socket.recv()
    #     data_py = self._deserializer.deserialize(data_b)
    #     return data_py

    # obj_A_msg = AnwClient(self._account_name, status)
