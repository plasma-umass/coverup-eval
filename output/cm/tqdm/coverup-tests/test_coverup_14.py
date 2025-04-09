# file tqdm/contrib/telegram.py:108-124
# lines []
# branches ['119->124']

import os
import pytest
from unittest.mock import patch
from tqdm.contrib.telegram import tqdm_telegram
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def mock_telegram_io(mocker):
    mocker.patch('tqdm.contrib.telegram.TelegramIO', autospec=True)

def test_tqdm_telegram_disable(mock_telegram_io):
    with patch.dict(os.environ, {'TQDM_TELEGRAM_TOKEN': 'fake_token', 'TQDM_TELEGRAM_CHAT_ID': 'fake_chat_id'}):
        tqdm_instance = tqdm_telegram(disable=True)
        assert not hasattr(tqdm_instance, 'tgio')
