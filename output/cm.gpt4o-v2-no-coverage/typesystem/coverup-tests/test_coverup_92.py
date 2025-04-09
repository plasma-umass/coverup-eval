# file: typesystem/base.py:201-204
# asked: {"lines": [204], "branches": [[202, 204]]}
# gained: {"lines": [204], "branches": [[202, 204]]}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_str_single_message_no_index():
    message = Message(text="Error message", index=None)
    error = BaseError(messages=[message])
    assert str(error) == "Error message"

def test_base_error_str_multiple_messages():
    message1 = Message(text="Error message 1", index=None)
    message2 = Message(text="Error message 2", index=None)
    error = BaseError(messages=[message1, message2])
    assert str(error) == str(dict(error))

def test_base_error_str_single_message_with_index():
    message = Message(text="Error message", index=[1])
    error = BaseError(messages=[message])
    assert str(error) == str(dict(error))
