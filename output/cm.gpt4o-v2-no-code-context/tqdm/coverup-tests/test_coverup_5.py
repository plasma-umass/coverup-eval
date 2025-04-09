# file: tqdm/contrib/telegram.py:108-124
# asked: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}
# gained: {"lines": [108, 119, 120, 121, 122, 123, 124], "branches": [[119, 120], [119, 124]]}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_telegram_io():
    with patch('tqdm.contrib.telegram.TelegramIO') as mock:
        yield mock

def test_tqdm_telegram_init_with_kwargs(mock_telegram_io):
    token = 'test_token'
    chat_id = 'test_chat_id'
    kwargs = {'token': token, 'chat_id': chat_id, 'disable': False}

    with patch('tqdm.contrib.telegram.getenv', side_effect=lambda k: {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}[k]):
        tqdm = tqdm_telegram(**kwargs)

    mock_telegram_io.assert_called_once_with(token, chat_id)
    assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_without_kwargs(mock_telegram_io):
    token = 'env_token'
    chat_id = 'env_chat_id'
    kwargs = {'disable': False}

    with patch('tqdm.contrib.telegram.getenv', side_effect=lambda k: {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}[k]):
        tqdm = tqdm_telegram(**kwargs)

    mock_telegram_io.assert_called_once_with(token, chat_id)
    assert hasattr(tqdm, 'tgio')

def test_tqdm_telegram_init_disabled(mock_telegram_io):
    kwargs = {'disable': True}

    tqdm = tqdm_telegram(**kwargs)

    mock_telegram_io.assert_not_called()
    assert not hasattr(tqdm, 'tgio')
