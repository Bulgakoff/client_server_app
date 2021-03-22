import pytest
from m_chat.send_buffer import SendBuffer


def test_send():
    exp_data = b'qweqweasdasd'
    enter_data = b'qweqweasdasd'
    sut = SendBuffer()
    sut.send(enter_data)

    assert sut._out_data == exp_data




