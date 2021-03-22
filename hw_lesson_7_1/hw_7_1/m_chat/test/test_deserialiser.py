import pytest
from m_chat.deserializer \
    import Deserializer

import json


def test_deserialize_responce():
    # msg = b"123123test"

    exit_msg_py_1 = {"response": "200",
                    "alert": "okok"}

    enter_msg_bytes = json.dumps(exit_msg_py_1).\
        encode('utf-8')
    msg_str = enter_msg_bytes.decode('utf-8')
    # =====--------------------------
    exit_msg_py_2 = json.loads(msg_str)
    sut = Deserializer()
    assert sut.deserialize(enter_msg_bytes) == exit_msg_py_2
