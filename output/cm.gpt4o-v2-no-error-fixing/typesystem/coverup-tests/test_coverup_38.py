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
    messages = [Message(text="Error 1", key="key1"), Message(text="Error 2", key="key2")]
    error = BaseError(messages=messages)
    assert len(error) == len(error._message_dict)
