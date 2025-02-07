# file: typesystem/base.py:81-83
# asked: {"lines": [81, 82, 83], "branches": []}
# gained: {"lines": [81, 82, 83], "branches": []}

import pytest
from typesystem.base import Message

def test_message_hash():
    # Create a Message instance with specific code and index
    message = Message(text="Error message", code="error_code", index=["index1", "index2"])
    
    # Calculate the hash
    message_hash = hash(message)
    
    # Verify the hash is as expected
    expected_ident = ("error_code", ("index1", "index2"))
    assert message_hash == hash(expected_ident)

    # Clean up
    del message

def test_message_hash_no_code():
    # Create a Message instance with default code and specific index
    message = Message(text="Error message", index=["index1", "index2"])
    
    # Calculate the hash
    message_hash = hash(message)
    
    # Verify the hash is as expected
    expected_ident = ("custom", ("index1", "index2"))
    assert message_hash == hash(expected_ident)

    # Clean up
    del message

def test_message_hash_empty_index():
    # Create a Message instance with specific code and empty index
    message = Message(text="Error message", code="error_code")
    
    # Calculate the hash
    message_hash = hash(message)
    
    # Verify the hash is as expected
    expected_ident = ("error_code", ())
    assert message_hash == hash(expected_ident)

    # Clean up
    del message
