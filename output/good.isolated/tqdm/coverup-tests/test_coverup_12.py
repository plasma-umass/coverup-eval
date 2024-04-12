# file tqdm/contrib/telegram.py:136-139
# lines [136, 137, 138, 139]
# branches ['138->exit', '138->139']

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram, tqdm_auto

@pytest.fixture
def mock_tgio():
    mock = MagicMock()
    mock.message_id = None
    return mock

@pytest.fixture
def mock_super_clear(mocker):
    return mocker.patch('tqdm.std.tqdm.clear', return_value=None)

def test_tqdm_telegram_clear(mock_tgio, mock_super_clear):
    # Patch the TelegramIO to avoid network calls
    with patch('tqdm.contrib.telegram.TelegramIO', return_value=mock_tgio):
        # Create an instance of tqdm_telegram with the mocked tgio
        with tqdm_telegram(total=100, disable=False) as t:
            # Call the clear method
            t.clear()

            # Check if super().clear() was called
            mock_super_clear.assert_called_once()

            # Check if tgio.write("") was called
            mock_tgio.write.assert_called_with("")

            # Reset mock to clear the call count
            mock_tgio.write.reset_mock()

            # Now test with disable=True
            t.disable = True
            t.clear()

            # Check if tgio.write("") was not called again
            mock_tgio.write.assert_not_called()
