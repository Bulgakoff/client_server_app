import json
import time

from m_chat.serializer \
    import Serializer
from m_chat.messages \
    import Authenticate, Responce,AnwQuit


def test_serialise_authenticate():
    msg = Authenticate('Alex', 'passw')
    expected_time = 124
    expected_msg_py = {
        'action': 'authenticate',
        # 'action': 'dfgdfg',
        'time': expected_time,
        'user': {
            'account_name': msg.account_name,
            'password': msg.password
        }
    }
    expected_data_bytes = json.dumps(expected_msg_py).encode('utf-8')
    sut = Serializer(get_time_foo=lambda: expected_time)
    assert sut.serialize(msg) == expected_data_bytes


def test_serialise_response_from_server():
    obj_Resp_msg = Responce('200', 'okey')
    exp_qwe = 1233
    expected_msg_py = {
        "response": obj_Resp_msg.response,
        "alert": obj_Resp_msg.alert
    }
    expected_data_bytes = json.dumps(expected_msg_py) \
        .encode('utf-8')

    sut = Serializer(get_time_foo=lambda: exp_qwe)
    assert sut.serialize(obj_Resp_msg) == expected_data_bytes


def test_serialise_quit():
    obj_Qu_msg = AnwQuit('402')
    # exp_qwe = 1233
    expected_msg_py = {
        "action": "quit"
    }
    expected_data_bytes = json.dumps(expected_msg_py) \
        .encode('utf-8')
    sut = Serializer()

    assert sut.serialize(obj_Qu_msg) == expected_data_bytes

