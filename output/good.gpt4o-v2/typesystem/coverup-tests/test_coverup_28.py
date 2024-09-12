# file: typesystem/base.py:201-204
# asked: {"lines": [201, 202, 203, 204], "branches": [[202, 203], [202, 204]]}
# gained: {"lines": [201, 202, 203, 204], "branches": [[202, 203], [202, 204]]}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_str_single_message():
    # Create a BaseError instance with a single message
    message = Message(text="Single error message", index=[])
    error = BaseError(messages=[message])
    
    # Assert that the __str__ method returns the message text
    assert str(error) == "Single error message"

def test_base_error_str_multiple_messages():
    # Create a BaseError instance with multiple messages
    message1 = Message(text="First error message", index=["field1"])
    message2 = Message(text="Second error message", index=["field2"])
    error = BaseError(messages=[message1, message2])
    
    # Assert that the __str__ method returns the string representation of the message dictionary
    assert str(error) == "{'field1': 'First error message', 'field2': 'Second error message'}"
