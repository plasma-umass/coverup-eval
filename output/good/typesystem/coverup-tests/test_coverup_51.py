# file typesystem/base.py:81-83
# lines [81, 82, 83]
# branches []

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    return Message(code="test_code", index=[1, 2, 3], text="test message")

def test_message_hash(message):
    # Ensure that the hash is consistent for the same message
    first_hash = hash(message)
    second_hash = hash(message)
    assert first_hash == second_hash

    # Ensure that different messages have different hashes
    different_message = Message(code="test_code", index=[1, 2, 4], text="test message")
    different_hash = hash(different_message)
    assert first_hash != different_hash

    # Cleanup is not necessary as Message instances do not modify any shared state
