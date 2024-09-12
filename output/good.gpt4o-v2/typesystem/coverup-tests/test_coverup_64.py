# file: typesystem/base.py:181-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_len():
    # Create a BaseError instance with a single message
    message = Message(text="Error message", code="error_code", key="key")
    error = BaseError(messages=[message])
    
    # Assert that the length of the error's message dictionary is 1
    assert len(error) == 1

    # Create a BaseError instance with multiple messages
    messages = [
        Message(text="Error message 1", code="error_code_1", key="key1"),
        Message(text="Error message 2", code="error_code_2", key="key2")
    ]
    error = BaseError(messages=messages)
    
    # Assert that the length of the error's message dictionary is equal to the number of messages
    assert len(error) == len(messages)
