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

def test_tqdm_telegram_init_with_kwargs(mock_getenv):
    with patch('tqdm.contrib.telegram.TelegramIO') as MockTelegramIO:
        mock_tgio_instance = MagicMock()
        MockTelegramIO.return_value = mock_tgio_instance

        kwargs = {
            'token': 'explicit_token',
            'chat_id': 'explicit_chat_id',
            'disable': False
        }
        tqdm_instance = tqdm_telegram(**kwargs)

        MockTelegramIO.assert_called_once_with('explicit_token', 'explicit_chat_id')
        assert tqdm_instance.tgio == mock_tgio_instance

def test_tqdm_telegram_init_without_kwargs(mock_getenv):
    with patch('tqdm.contrib.telegram.TelegramIO') as MockTelegramIO:
        mock_tgio_instance = MagicMock()
        MockTelegramIO.return_value = mock_tgio_instance

        kwargs = {
            'disable': False
        }
        tqdm_instance = tqdm_telegram(**kwargs)

        MockTelegramIO.assert_called_once_with('test_token', 'test_chat_id')
        assert tqdm_instance.tgio == mock_tgio_instance

def test_tqdm_telegram_init_disabled(mock_getenv):
    with patch('tqdm.contrib.telegram.TelegramIO') as MockTelegramIO:
        kwargs = {
            'disable': True
        }
        tqdm_instance = tqdm_telegram(**kwargs)

        MockTelegramIO.assert_not_called()
        assert not hasattr(tqdm_instance, 'tgio')
