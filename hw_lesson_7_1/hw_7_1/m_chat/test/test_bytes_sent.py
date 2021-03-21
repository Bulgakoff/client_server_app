import pytest
from m_chat.send_buffer import SendBuffer


def test_bytes_sent():
    class MyTestSendBuffer:
        _out_data = b''

        def send(self, data):
            self._out_data += data

        def bytes_sent(self, size):
            self._out_data=self._out_data[size:]


    mock_send_buff = MyTestSendBuffer()
    mock_send_buff.send(b'qweqweasdasd')
    mock_send_buff.bytes_sent(5)
    expected_data = b'easdasd'


    assert mock_send_buff._out_data==expected_data



