# qwe = b'qweqweasdasd'
# asd = qwe[5:]
# print(asd)#b'easdasd'
# expected_msg_py = {
#         'action': 'authenticate',
#         # 'action': 'dfgdfg',
#         'time': 3434,
#         'user': {
#             'account_name': 'msg.account_name',
#             'password': 4444444444444444
#         }
#     }
# print(expected_msg_py['user']['account_name'])
#
# Dmitry Erlikh, [15.03.21 16:00]
import pytest
from m_chat.messages import *
from m_chat.msg_parser import *

@pytest.mark.parametrize("msg_dict,expected",[({"action": "quit"},
                                               AnwQuit("quit"))])
def test_parseeeeeeeeeeeeeeee(msg_dict, expected):
    sut = MsgParser()
    assert sut.parse(msg_dict) == expected




    # остальные

