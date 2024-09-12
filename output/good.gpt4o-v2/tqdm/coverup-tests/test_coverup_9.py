# file: tqdm/contrib/telegram.py:141-146
# asked: {"lines": [141, 142, 143, 144, 145, 146], "branches": [[142, 143], [142, 144], [145, 0], [145, 146]]}
# gained: {"lines": [141, 142, 143, 144, 145, 146], "branches": [[142, 143], [142, 144], [145, 0], [145, 146]]}

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_tgio():
    with patch('tqdm.contrib.telegram.TelegramIO') as MockClass:
        instance = MockClass.return_value
        yield instance

def test_tqdm_telegram_close_disable(mock_tgio):
    # Create an instance with disable=True
    tqdm = tqdm_telegram(disable=True)
    tqdm.close()
    # Ensure tgio.delete() is not called
    mock_tgio.delete.assert_not_called()

def test_tqdm_telegram_close_not_leave(mock_tgio):
    # Create an instance with disable=False and leave=False
    tqdm = tqdm_telegram(disable=False, leave=False)
    tqdm.close()
    # Ensure tgio.delete() is called
    mock_tgio.delete.assert_called_once()

def test_tqdm_telegram_close_leave(mock_tgio):
    # Create an instance with disable=False and leave=True
    tqdm = tqdm_telegram(disable=False, leave=True)
    tqdm.close()
    # Ensure tgio.delete() is not called
    mock_tgio.delete.assert_not_called()

def test_tqdm_telegram_close_leave_none_pos_zero(mock_tgio):
    # Create an instance with disable=False, leave=None, and pos=0
    tqdm = tqdm_telegram(disable=False, leave=None, position=0)
    tqdm.close()
    # Ensure tgio.delete() is not called
    mock_tgio.delete.assert_not_called()

def test_tqdm_telegram_close_leave_none_pos_nonzero(mock_tgio):
    # Create an instance with disable=False, leave=None, and pos=1
    tqdm = tqdm_telegram(disable=False, leave=None, position=1)
    tqdm.close()
    # Ensure tgio.delete() is called
    mock_tgio.delete.assert_called_once()
