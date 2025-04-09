# file: tqdm/contrib/telegram.py:108-124
# asked: {"lines": [119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}
# gained: {"lines": [119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram
from os import getenv

class TelegramIO:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

@pytest.fixture
def mock_telegram_io(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('tqdm.contrib.telegram.TelegramIO', mock)
    return mock

def test_tqdm_telegram_init_with_kwargs(mock_telegram_io):
    token = 'test_token'
    chat_id = 'test_chat_id'
    with patch.dict('os.environ', {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}):
        tqdm = tqdm_telegram(token=token, chat_id=chat_id, disable=False)
        mock_telegram_io.assert_called_once_with(token, chat_id)
        assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_without_kwargs(mock_telegram_io):
    token = 'env_token'
    chat_id = 'env_chat_id'
    with patch.dict('os.environ', {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}):
        tqdm = tqdm_telegram(disable=False)
        mock_telegram_io.assert_called_once_with(token, chat_id)
        assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_disable(mock_telegram_io):
    tqdm = tqdm_telegram(disable=True)
    mock_telegram_io.assert_not_called()
    assert not hasattr(tqdm, 'tgio')
