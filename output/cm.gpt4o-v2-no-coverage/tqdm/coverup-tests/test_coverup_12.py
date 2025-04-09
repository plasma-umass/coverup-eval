# file: tqdm/contrib/telegram.py:141-146
# asked: {"lines": [141, 142, 143, 144, 145, 146], "branches": [[142, 143], [142, 144], [145, 0], [145, 146]]}
# gained: {"lines": [141, 142, 143, 144, 145, 146], "branches": [[142, 143], [142, 144], [145, 0], [145, 146]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_tqdm_telegram():
    with patch('tqdm.contrib.telegram.TelegramIO') as MockTelegramIO:
        instance = tqdm_telegram(token='dummy_token', chat_id='dummy_chat_id', disable=False)
        instance.tgio = MockTelegramIO.return_value
        yield instance

def test_close_disable(mock_tqdm_telegram):
    mock_tqdm_telegram.disable = True
    mock_tqdm_telegram.close()
    mock_tqdm_telegram.tgio.delete.assert_not_called()

def test_close_enable_leave(mock_tqdm_telegram):
    mock_tqdm_telegram.disable = False
    mock_tqdm_telegram.leave = True
    mock_tqdm_telegram.close()
    mock_tqdm_telegram.tgio.delete.assert_not_called()

def test_close_enable_leave_none_pos_not_zero(mock_tqdm_telegram):
    mock_tqdm_telegram.disable = False
    mock_tqdm_telegram.leave = None
    mock_tqdm_telegram.pos = 1
    mock_tqdm_telegram.close()
    mock_tqdm_telegram.tgio.delete.assert_called_once()

def test_close_enable_leave_none_pos_zero(mock_tqdm_telegram):
    mock_tqdm_telegram.disable = False
    mock_tqdm_telegram.leave = None
    mock_tqdm_telegram.pos = 0
    mock_tqdm_telegram.close()
    mock_tqdm_telegram.tgio.delete.assert_not_called()
