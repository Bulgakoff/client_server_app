import pytest
import json
from m_chat.msg_parser \
    import MsgParser

def test_parse():
    level_1 = {"response": "200",
                     "alert": "okok"}

    level_2 = json.dumps(level_1). \
        encode('utf-8')# bytes
    # =====--------------------------

    enter_json = level_2.decode('utf-8')
    exit_msg_py_2 = json.loads(enter_json)
    sut = MsgParser()
    assert sut.parse(enter_json) == level_1