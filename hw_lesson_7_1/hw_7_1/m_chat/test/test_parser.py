import pytest
import json
from m_chat.msg_parser \
    import MsgParser
from m_chat.messages import *

def test_parse():
    msg_obj= AnwQuit('quit')
    msg_obj2= Responce('200','ok')
    msg_obj3= Authenticate('Bob','password_my')
    sut = MsgParser()
    sut2 = MsgParser()
    sut3 = MsgParser()
    qwe1 = {"action": "quit"}
    qwe2 = {"response": "200",
            "alert": "ok"}
    qwe3 = {
        'action': 'authenticate',
        # 'action': 'dfgdfg',
        'time': 'expected_time',
        'user': {
            'account_name': 'Bob',
            'password': 'password_my'
        }
    }

    sut.parse(qwe1)
    sut2.parse(qwe2)
    sut3.parse(qwe3)

    assert sut.parse(qwe1)==msg_obj
    assert sut2.parse(qwe2)==msg_obj2
    assert sut3.parse(qwe3)==msg_obj3
