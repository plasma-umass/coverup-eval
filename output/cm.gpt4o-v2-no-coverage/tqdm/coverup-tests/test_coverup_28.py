# file: tqdm/contrib/telegram.py:136-139
# asked: {"lines": [137, 138, 139], "branches": [[138, 0], [138, 139]]}
# gained: {"lines": [137, 138, 139], "branches": [[138, 0], [138, 139]]}

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
    tg = tqdm_telegram(token='dummy_token', chat_id='dummy_chat_id', disable=False)
    tg.tgio = mock_tgio  # Inject mock TelegramIO instance

    # Reset mock call history to avoid interference from __init__
    mock_tgio.write.reset_mock()

    # Call the clear method
    tg.clear()

    # Assert that the clear method of the superclass was called
    assert tg.n == 0  # This is a side effect of calling clear in tqdm

    # Assert that tgio.write was called with an empty string
    mock_tgio.write.assert_called_once_with("")

def test_tqdm_telegram_clear_disabled(mock_tgio):
    # Create an instance of tqdm_telegram with disable=True
    tg = tqdm_telegram(token='dummy_token', chat_id='dummy_chat_id', disable=True)
    tg.tgio = mock_tgio  # Inject mock TelegramIO instance

    # Reset mock call history to avoid interference from __init__
    mock_tgio.write.reset_mock()

    # Call the clear method
    tg.clear()

    # Assert that the clear method of the superclass was called
    assert tg.n == 0  # This is a side effect of calling clear in tqdm

    # Assert that tgio.write was not called
    mock_tgio.write.assert_not_called()
