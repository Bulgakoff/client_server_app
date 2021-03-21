from m_chat.messages \
    import Authenticate,\
    Responce,ResponceError, AnwClient,AnwQuit
import time
import json
from m_chat.deserializer import Deserializer


class Serializer:
    def __init__(self, dumps=json.dumps,
                 encodding='utf-8',
                 get_time_foo=time.ctime):
        self._dumps = dumps
        self._encodding = encodding
        self._get_time_foo = get_time_foo

    def serialize(self, obj_A_msg):
        if isinstance(obj_A_msg, Authenticate):
            result_py = {
                'action': 'authenticate',
                # 'action': 'dfgdfg',
                'time': self._get_time_foo(),
                'user': {
                    'account_name': obj_A_msg.account_name,
                    'password': obj_A_msg.password
                }
            }
            result_str = self._dumps(result_py)
            result_byte = result_str.encode(self._encodding)
            return result_byte
        elif isinstance(obj_A_msg, Responce):
            result_py = {
                "response": obj_A_msg.response,
                "alert": obj_A_msg.alert
            }
            result_str = self._dumps(result_py)
            result_byte = result_str.encode(self._encodding)
            return result_byte
        elif isinstance(obj_A_msg, ResponceError):
            result_py = {
                "response": obj_A_msg.response,
                "error": obj_A_msg.error
            }
            result_str = self._dumps(result_py)
            result_byte = result_str.encode(self._encodding)
            return result_byte
        elif isinstance(obj_A_msg, AnwClient):
            result_py = {
                'action': 'presence',
                # 'action': 'dfgdfg',
                'time': self._get_time_foo(),
                'user': {
                    'account_name': obj_A_msg.account_name,
                    'status': obj_A_msg.status
                }
            }
            result_str = self._dumps(result_py)
            result_byte = result_str.encode(self._encodding)
            return result_byte
        elif isinstance(obj_A_msg, AnwQuit):
            result_py = {
                'action': 'quit',
            }
            result_str = self._dumps(result_py)
            result_byte = result_str.encode(self._encodding)
            return result_byte

