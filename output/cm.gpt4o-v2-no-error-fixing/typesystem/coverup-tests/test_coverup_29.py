# file: typesystem/base.py:190-192
# asked: {"lines": [190, 191, 192], "branches": []}
# gained: {"lines": [190, 191, 192], "branches": []}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_hash():
    # Create a BaseError instance with a list of messages
    messages = [Message(text="Error 1"), Message(text="Error 2")]
    error = BaseError(messages=messages)
    
    # Calculate the hash
    error_hash = hash(error)
    
    # Verify that the hash is an integer
    assert isinstance(error_hash, int)
    
    # Verify that the hash is consistent
    assert error_hash == hash(error)
