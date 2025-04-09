# file: tqdm/contrib/telegram.py:108-124
# asked: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}
# gained: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}

import pytest
from os import getenv
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram

class MockedTelegramIO:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def write(self, s):
        pass

    def delete(self):
        pass

@pytest.fixture
def mock_telegram_io(monkeypatch):
    monkeypatch.setattr('tqdm.contrib.telegram.TelegramIO', MockedTelegramIO)

def test_tqdm_telegram_init_with_token_and_chat_id(mock_telegram_io):
    token = 'test_token'
    chat_id = 'test_chat_id'
    with patch.dict('os.environ', {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}):
        tqdm = tqdm_telegram(token=token, chat_id=chat_id)
        assert tqdm.tgio.token == token
        assert tqdm.tgio.chat_id == chat_id

def test_tqdm_telegram_init_with_env_vars(mock_telegram_io):
    token = 'env_token'
    chat_id = 'env_chat_id'
    with patch.dict('os.environ', {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}):
        tqdm = tqdm_telegram()
        assert tqdm.tgio.token == token
        assert tqdm.tgio.chat_id == chat_id

def test_tqdm_telegram_init_with_disable(mock_telegram_io):
    tqdm = tqdm_telegram(disable=True)
    assert not hasattr(tqdm, 'tgio')
