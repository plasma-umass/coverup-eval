# file: tqdm/contrib/telegram.py:31-38
# asked: {"lines": [31, 33, 34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [31, 33, 34, 35, 36, 37, 38], "branches": []}

import pytest
from requests import Session
from tqdm.contrib.telegram import TelegramIO

class MockSession:
    def post(self, url, data):
        class MockResponse:
            def json(self):
                return {'result': {'message_id': 12345}}
        return MockResponse()

def test_telegram_io_init(monkeypatch):
    # Arrange
    token = "test_token"
    chat_id = "test_chat_id"
    
    # Mock the Session object to avoid real HTTP requests
    monkeypatch.setattr("tqdm.contrib.telegram.Session", MockSession)
    
    # Act
    telegram_io = TelegramIO(token, chat_id)
    
    # Assert
    assert telegram_io.token == token
    assert telegram_io.chat_id == chat_id
    assert isinstance(telegram_io.session, MockSession)
    assert telegram_io.text == "TelegramIO"
    assert hasattr(telegram_io, 'message_id')
    assert telegram_io.message_id == 12345
