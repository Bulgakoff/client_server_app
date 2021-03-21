import pytest
from m_chat.messages import *
from m_chat.message_processor \
    import MessageProcessor


def test_on_auth_response():
    qwe_1 = Responce('200','ok')
    qwe_err = ResponceError('402','no-o-o-o')

    expected_msg_py = {
        "response": qwe_1.response,
        "alert": qwe_1.alert
    }
    expected_msg_py_err = {
        "response": qwe_err.response,
        "error": qwe_err.error
    }
    sut_1 = MessageProcessor()
    sut_2 = MessageProcessor()
    assert sut_1.on_auth_response(qwe_1)==expected_msg_py
    assert sut_2.on_auth_response(qwe_err)==expected_msg_py_err


