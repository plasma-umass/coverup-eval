# file typesystem/base.py:72-79
# lines [72, 73, 74, 75, 76, 77, 78]
# branches []

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    return Message(text="Error", code="error_code", index=1, start_position=0, end_position=4)

def test_message_equality(message):
    # Create another message with the same properties
    same_message = Message(text="Error", code="error_code", index=1, start_position=0, end_position=4)
    # Create a message with different properties
    different_message = Message(text="Different", code="diff_code", index=2, start_position=1, end_position=5)

    # Test equality
    assert message == same_message
    assert message != different_message
    assert message != "not_a_message"  # Different type should not be equal

    # Clean up is not necessary as no external state is modified
