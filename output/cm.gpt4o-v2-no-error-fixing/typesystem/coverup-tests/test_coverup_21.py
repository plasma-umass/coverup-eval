# file: typesystem/base.py:201-204
# asked: {"lines": [201, 202, 203, 204], "branches": [[202, 203], [202, 204]]}
# gained: {"lines": [201, 202, 203, 204], "branches": [[202, 203], [202, 204]]}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_str_single_message():
    message = Message(text="Single error message", index=[])
    error = BaseError(messages=[message])
    assert str(error) == "Single error message"

def test_base_error_str_multiple_messages():
    message1 = Message(text="First error message", index=[1])
    message2 = Message(text="Second error message", index=[2])
    error = BaseError(messages=[message1, message2])
    assert str(error) == str({1: "First error message", 2: "Second error message"})
