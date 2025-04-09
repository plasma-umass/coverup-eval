# file: typesystem/base.py:81-83
# asked: {"lines": [81, 82, 83], "branches": []}
# gained: {"lines": [81, 82, 83], "branches": []}

import pytest
from typesystem.base import Message

def test_message_hash():
    # Create a Message instance with code and index
    message = Message(text="Error message", code="error_code", index=["users", 3, "username"])
    
    # Calculate the hash
    message_hash = hash(message)
    
    # Verify the hash is as expected
    expected_ident = ("error_code", ("users", 3, "username"))
    assert message_hash == hash(expected_ident)

    # Clean up
    del message
