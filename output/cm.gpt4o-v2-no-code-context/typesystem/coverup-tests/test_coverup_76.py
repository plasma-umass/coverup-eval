# file: typesystem/base.py:201-204
# asked: {"lines": [204], "branches": [[202, 204]]}
# gained: {"lines": [204], "branches": [[202, 204]]}

import pytest
from typesystem.base import BaseError

class MockMessage:
    def __init__(self, text, index=None):
        self.text = text
        self.index = index

@pytest.fixture
def base_error_single_message(monkeypatch):
    error = BaseError(text="Single message")
    monkeypatch.setattr(error, '_messages', [MockMessage("Single message", None)])
    return error

@pytest.fixture
def base_error_multiple_messages(monkeypatch):
    error = BaseError(messages=[MockMessage("First message", [1]), MockMessage("Second message", [2])])
    monkeypatch.setattr(error, '_messages', [MockMessage("First message", [1]), MockMessage("Second message", [2])])
    return error

def test_base_error_str_single_message(base_error_single_message):
    assert str(base_error_single_message) == "Single message"

def test_base_error_str_multiple_messages(base_error_multiple_messages):
    result = str(base_error_multiple_messages)
    assert result.startswith("{")
    assert "'First message'" in result
    assert "'Second message'" in result
    assert result.endswith("}")
