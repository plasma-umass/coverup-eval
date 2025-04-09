# file: typesystem/base.py:81-83
# asked: {"lines": [81, 82, 83], "branches": []}
# gained: {"lines": [81, 82, 83], "branches": []}

import pytest
from typesystem.base import Message

def test_message_hash():
    # Create instances of Message
    msg1 = Message(text="Error message", code="error_code", index=[1, 2])
    msg2 = Message(text="Another message", code="error_code", index=[1, 2])
    msg3 = Message(text="Different message", code="different_code", index=[3, 4])

    # Check that identical messages have the same hash
    assert hash(msg1) == hash(msg2)

    # Check that different messages have different hashes
    assert hash(msg1) != hash(msg3)
    assert hash(msg2) != hash(msg3)
