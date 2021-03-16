from m_chat.messages import *
from m_chat.message_processor import MessageProcessor

class MessageHandler:
    def __init__(self, message_processor):
        self._message_processor = message_processor

    def on_msg(self, msg):
        if isinstance(msg, Responce):
            self._message_processor.on_auth_response(msg)

