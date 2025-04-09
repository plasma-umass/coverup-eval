# file tqdm/contrib/telegram.py:27-30
# lines [27, 28, 29]
# branches []

import pytest
from unittest.mock import patch
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def mock_telegram_io():
    with patch('tqdm.contrib.telegram.TelegramIO') as mock:
        yield mock

def test_telegram_io_api(mock_telegram_io):
    assert TelegramIO.API == 'https://api.telegram.org/bot'
    mock_telegram_io.assert_not_called()  # Ensure TelegramIO is not instantiated
