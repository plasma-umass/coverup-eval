# file tqdm/contrib/telegram.py:108-124
# lines [108, 119, 120, 121, 122, 123, 124]
# branches ['119->120', '119->124']

import pytest
from unittest.mock import patch, MagicMock
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_telegram_io():
    with patch('tqdm.contrib.telegram.TelegramIO') as mock:
        yield mock

def test_tqdm_telegram_initialization(mock_telegram_io):
    token = 'test_token'
    chat_id = 'test_chat_id'
    
    # Mock environment variables
    with patch('tqdm.contrib.telegram.getenv', side_effect=lambda k: {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}.get(k)):
        # Initialize tqdm_telegram with token and chat_id
        progress = tqdm_telegram(token=token, chat_id=chat_id)
        
        # Assertions to verify TelegramIO is initialized correctly
        mock_telegram_io.assert_called_once_with(token, chat_id)
        assert progress.tgio is not None

def test_tqdm_telegram_initialization_with_env_vars(mock_telegram_io):
    token = 'env_token'
    chat_id = 'env_chat_id'
    
    # Mock environment variables
    with patch('tqdm.contrib.telegram.getenv', side_effect=lambda k: {'TQDM_TELEGRAM_TOKEN': token, 'TQDM_TELEGRAM_CHAT_ID': chat_id}.get(k)):
        # Initialize tqdm_telegram without token and chat_id to use env vars
        progress = tqdm_telegram()
        
        # Assertions to verify TelegramIO is initialized correctly
        mock_telegram_io.assert_called_once_with(token, chat_id)
        assert progress.tgio is not None

def test_tqdm_telegram_disable(mock_telegram_io):
    # Initialize tqdm_telegram with disable=True
    progress = tqdm_telegram(disable=True)
    
    # Assertions to verify TelegramIO is not initialized
    mock_telegram_io.assert_not_called()
    assert not hasattr(progress, 'tgio')
