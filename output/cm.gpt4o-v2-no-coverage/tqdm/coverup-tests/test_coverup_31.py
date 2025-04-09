# file: tqdm/contrib/telegram.py:80-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": []}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": []}

import pytest
from unittest.mock import Mock, patch
from tqdm.contrib.telegram import TelegramIO

@pytest.fixture
def telegram_io(monkeypatch):
    with patch.object(TelegramIO, 'message_id', new_callable=Mock) as mock_message_id:
        mock_message_id.return_value = "dummy_message_id"
        yield TelegramIO(token="dummy_token", chat_id="dummy_chat_id")

def test_delete_success(telegram_io, monkeypatch):
    mock_future = Mock()
    mock_submit = Mock(return_value=mock_future)
    monkeypatch.setattr(telegram_io, 'submit', mock_submit)
    
    future = telegram_io.delete()
    
    mock_submit.assert_called_once_with(
        telegram_io.session.post,
        telegram_io.API + '%s/deleteMessage' % telegram_io.token,
        data={'chat_id': telegram_io.chat_id, 'message_id': telegram_io.message_id}
    )
    assert future == mock_future

def test_delete_exception(telegram_io, monkeypatch):
    mock_submit = Mock(side_effect=Exception("Test exception"))
    monkeypatch.setattr(telegram_io, 'submit', mock_submit)
    mock_tqdm_write = Mock()
    monkeypatch.setattr('tqdm.auto.tqdm.write', mock_tqdm_write)
    
    future = telegram_io.delete()
    
    mock_submit.assert_called_once_with(
        telegram_io.session.post,
        telegram_io.API + '%s/deleteMessage' % telegram_io.token,
        data={'chat_id': telegram_io.chat_id, 'message_id': telegram_io.message_id}
    )
    mock_tqdm_write.assert_called_once_with("Test exception")
    assert future is None
