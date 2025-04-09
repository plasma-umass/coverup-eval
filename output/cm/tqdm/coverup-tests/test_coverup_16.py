# file tqdm/contrib/telegram.py:141-146
# lines [144, 145, 146]
# branches ['142->144', '145->exit', '145->146']

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram, TelegramIO

@pytest.fixture
def mock_tgio():
    mock = MagicMock(spec=TelegramIO)
    mock.delete = MagicMock()
    return mock

@pytest.fixture
def mock_tqdm_telegram(mock_tgio):
    with patch('tqdm.contrib.telegram.TelegramIO', return_value=mock_tgio):
        with tqdm_telegram(total=100) as tt:
            yield tt

def test_tqdm_telegram_close_with_leave_false(mock_tqdm_telegram, mock_tgio):
    mock_tqdm_telegram.leave = False
    mock_tqdm_telegram.pos = 1  # Ensure that leave is False and pos is not 0
    mock_tqdm_telegram.close()
    mock_tgio.delete.assert_called_once()

def test_tqdm_telegram_close_with_leave_none_pos_zero(mock_tqdm_telegram, mock_tgio):
    mock_tqdm_telegram.leave = None
    mock_tqdm_telegram.pos = 0  # Ensure that leave is None and pos is 0
    mock_tqdm_telegram.close()
    mock_tgio.delete.assert_not_called()
