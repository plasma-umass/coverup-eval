# file: typesystem/base.py:157-176
# asked: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}
# gained: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_messages_no_prefix():
    # Create a BaseError instance with a list of messages
    messages = [
        Message(text="Error 1", code="code1", index=[1]),
        Message(text="Error 2", code="code2", index=[2])
    ]
    error = BaseError(messages=messages)
    
    # Call the messages method without add_prefix
    result = error.messages()
    
    # Verify the result
    assert result == messages

def test_base_error_messages_with_prefix():
    # Create a BaseError instance with a list of messages
    messages = [
        Message(text="Error 1", code="code1", index=[1]),
        Message(text="Error 2", code="code2", index=[2])
    ]
    error = BaseError(messages=messages)
    
    # Call the messages method with add_prefix
    prefix = "prefix"
    result = error.messages(add_prefix=prefix)
    
    # Verify the result
    expected = [
        Message(text="Error 1", code="code1", index=[prefix, 1]),
        Message(text="Error 2", code="code2", index=[prefix, 2])
    ]
    assert result == expected
