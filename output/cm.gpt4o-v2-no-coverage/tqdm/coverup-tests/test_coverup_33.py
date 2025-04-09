# file: tqdm/contrib/telegram.py:59-78
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78], "branches": [[61, 62], [61, 63], [64, 65], [64, 66], [67, 68], [67, 69]]}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 78], "branches": [[61, 62], [61, 63], [64, 65], [64, 66], [67, 69]]}

import pytest
from unittest.mock import Mock, patch
from requests import Session
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def telegram_io(mocker):
    mocker.patch('tqdm.contrib.telegram.TelegramIO.message_id', new_callable=mocker.PropertyMock, return_value=123)
    return TelegramIO(token="dummy_token", chat_id="dummy_chat_id")

def test_write_empty_string(telegram_io, mocker):
    telegram_io.write("")
    assert telegram_io.text == "..."

def test_write_same_text(telegram_io, mocker):
    telegram_io.text = "test"
    telegram_io.write("test")
    assert telegram_io.text == "test"

def test_write_new_text(telegram_io, mocker):
    mocker.patch.object(telegram_io, 'submit', return_value="future")
    future = telegram_io.write("new text")
    assert telegram_io.text == "new text"
    assert future == "future"

def test_write_exception(telegram_io, mocker):
    mocker.patch.object(telegram_io, 'submit', side_effect=Exception("error"))
    mock_tqdm_write = mocker.patch('tqdm.auto.tqdm.write')
    telegram_io.write("new text")
    mock_tqdm_write.assert_called_once_with("error")
