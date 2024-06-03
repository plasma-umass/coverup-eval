# file tqdm/contrib/telegram.py:31-38
# lines [31, 33, 34, 35, 36, 37, 38]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def mock_session(mocker):
    return mocker.patch('tqdm.contrib.telegram.Session', autospec=True)

def test_telegram_io_initialization(mock_session):
    token = 'dummy_token'
    chat_id = 'dummy_chat_id'
    
    telegram_io = TelegramIO(token, chat_id)
    
    assert telegram_io.token == token
    assert telegram_io.chat_id == chat_id
    assert telegram_io.text == 'TelegramIO'
    assert hasattr(telegram_io, 'message_id')
    assert telegram_io.session is mock_session.return_value
