# file: tqdm/contrib/telegram.py:31-38
# asked: {"lines": [33, 34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [33, 34, 35, 36, 37, 38], "branches": []}

import pytest
from requests import Session
from tqdm.contrib.telegram import TelegramIO
from tqdm.contrib.utils_worker import MonoWorker

class MockSession:
    def __init__(self):
        self.data = None

    def post(self, url, data):
        self.data = data
        return self

    def json(self):
        return {"ok": True, "result": {"message_id": 123}}

@pytest.fixture
def mock_session(monkeypatch):
    mock = MockSession()
    monkeypatch.setattr(Session, "__new__", lambda cls: mock)
    return mock

def test_telegram_io_init(mock_session):
    token = "test_token"
    chat_id = "test_chat_id"
    telegram_io = TelegramIO(token, chat_id)

    assert telegram_io.token == token
    assert telegram_io.chat_id == chat_id
    assert isinstance(telegram_io.session, MockSession)
    assert telegram_io.text == "TelegramIO"
    assert telegram_io.message_id is not None
