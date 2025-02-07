# file: tqdm/contrib/telegram.py:136-139
# asked: {"lines": [136, 137, 138, 139], "branches": [[138, 0], [138, 139]]}
# gained: {"lines": [136, 137, 138, 139], "branches": [[138, 0], [138, 139]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_tgio():
    with patch('tqdm.contrib.telegram.TelegramIO') as MockClass:
        instance = MockClass.return_value
        yield instance

def test_tqdm_telegram_clear(mock_tgio):
    # Create an instance of tqdm_telegram with disable=False
    tqdm_instance = tqdm_telegram(token='dummy_token', chat_id='dummy_chat_id', disable=False)
    
    # Mock the clear method of the parent class
    with patch.object(tqdm_telegram, 'clear', wraps=tqdm_instance.clear) as mock_clear:
        tqdm_instance.clear()
        mock_clear.assert_called_once()
    
    # Check that tgio.write was called
    assert mock_tgio.write.call_count == 2
    assert mock_tgio.write.call_args_list[-1] == (("",),)

def test_tqdm_telegram_clear_disabled(mock_tgio):
    # Create an instance of tqdm_telegram with disable=True
    tqdm_instance = tqdm_telegram(token='dummy_token', chat_id='dummy_chat_id', disable=True)
    
    # Mock the clear method of the parent class
    with patch.object(tqdm_telegram, 'clear', wraps=tqdm_instance.clear) as mock_clear:
        tqdm_instance.clear()
        mock_clear.assert_called_once()
    
    # Check that tgio.write was not called
    mock_tgio.write.assert_not_called()
