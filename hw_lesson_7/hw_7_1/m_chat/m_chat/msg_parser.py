import json
from dataclasses import dataclass


# делает из json py сообщения
class MsgParser:
    def __init__(self, loads=json.loads,
                 encodding='ascii'):
        self._loads = loads
        self._encodding = encodding

    def parse(self, parser_data_j):
        exit_msg_by = self._loads(parser_data_j)
        return exit_msg_by

