# file: tqdm/contrib/telegram.py:108-124
# asked: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}
# gained: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}

import pytest
from os import getenv
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram, TelegramIO

@pytest.fixture
def mock_getenv(monkeypatch):
    monkeypatch.setenv('TQDM_TELEGRAM_TOKEN', 'test_token')
    monkeypatch.setenv('TQDM_TELEGRAM_CHAT_ID', 'test_chat_id')

@pytest.fixture
def mock_telegram_io():
    with patch.object(TelegramIO, '__init__', return_value=None) as mock_tgio_init:
        with patch.object(TelegramIO, 'write', return_value=None) as mock_tgio_write:
            yield mock_tgio_init, mock_tgio_write

def test_tqdm_telegram_init_with_kwargs(mock_getenv, mock_telegram_io):
    mock_tgio_init, mock_tgio_write = mock_telegram_io
    tqdm = tqdm_telegram(token='token', chat_id='chat_id', disable=False)
    mock_tgio_init.assert_called_once_with('token', 'chat_id')
    assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_without_kwargs(mock_getenv, mock_telegram_io):
    mock_tgio_init, mock_tgio_write = mock_telegram_io
    tqdm = tqdm_telegram(disable=False)
    mock_tgio_init.assert_called_once_with('test_token', 'test_chat_id')
    assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_disabled(mock_getenv, mock_telegram_io):
    mock_tgio_init, mock_tgio_write = mock_telegram_io
    tqdm = tqdm_telegram(disable=True)
    mock_tgio_init.assert_not_called()
    assert not hasattr(tqdm, 'tgio')
