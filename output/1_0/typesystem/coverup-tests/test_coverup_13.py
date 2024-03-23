# file typesystem/base.py:81-83
# lines [81, 82, 83]
# branches []

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    return Message(code="test_code", text="Test message", index=[1, 2, 3])

def test_message_hash(message):
    # Ensure that the hash is consistent for the same message
    first_hash = hash(message)
    second_hash = hash(message)
    assert first_hash == second_hash

    # Ensure that the hash changes when the message changes
    message.index.append(4)
    third_hash = hash(message)
    assert first_hash != third_hash

    # Cleanup is not necessary as the message fixture is function-scoped
