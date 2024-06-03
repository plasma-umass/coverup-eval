# file tqdm/contrib/telegram.py:141-146
# lines [146]
# branches ['145->146']

import pytest
from unittest.mock import MagicMock, patch
from tqdm.contrib.telegram import tqdm_telegram

@pytest.fixture
def mock_tgio():
    with patch('tqdm.contrib.telegram.TelegramIO') as mock_class:
        mock_instance = mock_class.return_value
        mock_instance.delete = MagicMock()
        yield mock_instance

def test_tqdm_telegram_delete_called(mock_tgio):
    # Arrange
    tqdm_instance = tqdm_telegram()
    tqdm_instance.disable = False
    tqdm_instance.leave = False
    tqdm_instance.pos = 0
    tqdm_instance.tgio = mock_tgio

    # Act
    tqdm_instance.close()

    # Assert
    mock_tgio.delete.assert_called_once()

def test_tqdm_telegram_delete_not_called(mock_tgio):
    # Arrange
    tqdm_instance = tqdm_telegram()
    tqdm_instance.disable = False
    tqdm_instance.leave = True
    tqdm_instance.pos = 0
    tqdm_instance.tgio = mock_tgio

    # Act
    tqdm_instance.close()

    # Assert
    mock_tgio.delete.assert_not_called()
