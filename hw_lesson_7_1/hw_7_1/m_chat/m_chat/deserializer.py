
import json


class Deserializer:
    def __init__(self, loads=json.loads,
                 encodding='utf-8'):
        self._loads = loads
        self._encodding = encodding


    def deserialize(self, msg_bytes):
        msg_bytes_str = msg_bytes.decode(self._encodding)
        exit_msg_by = self._loads(msg_bytes_str)
        return exit_msg_by
