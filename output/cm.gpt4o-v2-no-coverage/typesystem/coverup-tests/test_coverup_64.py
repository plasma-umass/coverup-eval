# file: typesystem/base.py:181-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from typesystem.base import BaseError

class Message:
    def __init__(self, text, code=None, key=None, position=None):
        self.text = text
        self.code = code
        self.key = key
        self.position = position
        self.index = [key] if key is not None else []

def test_base_error_len():
    # Test with a single message
    message = Message(text="Error message", key="key1")
    error = BaseError(messages=[message])
    assert len(error) == 1

    # Test with multiple messages
    message1 = Message(text="Error message 1", key="key1")
    message2 = Message(text="Error message 2", key="key2")
    error = BaseError(messages=[message1, message2])
    assert len(error) == 2

    # Test with nested messages
    message1 = Message(text="Error message 1", key="key1")
    message2 = Message(text="Error message 2", key="key1")
    error = BaseError(messages=[message1, message2])
    assert len(error) == 1  # Since they share the same key, they are nested

