# file: typesystem/base.py:112-155
# asked: {"lines": [153], "branches": [[152, 153]]}
# gained: {"lines": [153], "branches": [[152, 153]]}

import pytest
from typesystem.base import BaseError, Message, Position

def test_base_error_single_message():
    message_text = "May not have more than 100 characters"
    error = BaseError(text=message_text)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == message_text
    assert error._message_dict == {"": message_text}

def test_base_error_multiple_messages():
    messages = [
        Message(text="Error 1", code="code1", index=["key1"]),
        Message(text="Error 2", code="code2", index=["key2", "subkey2"]),
    ]
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 2
    assert error._messages[0].text == "Error 1"
    assert error._messages[1].text == "Error 2"
    assert error._message_dict == {
        "key1": "Error 1",
        "key2": {
            "subkey2": "Error 2"
        }
    }

@pytest.fixture
def mock_message_class(monkeypatch):
    class MockMessage:
        def __init__(self, text, code=None, key=None, position=None, index=None):
            self.text = text
            self.code = code
            self.key = key
            self.position = position
            self.index = index or []

    monkeypatch.setattr("typesystem.base.Message", MockMessage)
    return MockMessage

def test_base_error_with_mock_message(mock_message_class):
    messages = [
        mock_message_class(text="Error 1", index=["key1"]),
        mock_message_class(text="Error 2", index=["key2", "subkey2"]),
    ]
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 2
    assert error._messages[0].text == "Error 1"
    assert error._messages[1].text == "Error 2"
    assert error._message_dict == {
        "key1": "Error 1",
        "key2": {
            "subkey2": "Error 2"
        }
    }
