# file: tqdm/contrib/telegram.py:31-38
# asked: {"lines": [31, 33, 34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [31, 33, 34, 35, 36, 37, 38], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def mock_session(monkeypatch):
    mock_session = MagicMock()
    monkeypatch.setattr('tqdm.contrib.telegram.Session', lambda: mock_session)
    return mock_session

def test_telegram_io_init(mock_session):
    token = 'dummy_token'
    chat_id = 'dummy_chat_id'
    
    with patch('tqdm.contrib.telegram.MonoWorker.__init__', return_value=None) as mock_init:
        telegram_io = TelegramIO(token, chat_id)
        
        mock_init.assert_called_once_with()
        assert telegram_io.token == token
        assert telegram_io.chat_id == chat_id
        assert telegram_io.session == mock_session
        assert telegram_io.text == 'TelegramIO'
        assert hasattr(telegram_io, 'message_id')
