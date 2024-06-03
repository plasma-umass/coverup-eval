# file typesystem/base.py:72-79
# lines [72, 73, 74, 75, 76, 77, 78]
# branches []

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    msg = Message(
        text="Error",
        code="E001",
        index=0,
        start_position=1,
        end_position=5
    )
    return msg

def test_message_equality(message):
    # Create an identical message
    identical_msg = Message(
        text="Error",
        code="E001",
        index=0,
        start_position=1,
        end_position=5
    )

    # Create a different message
    different_msg = Message(
        text="Warning",
        code="W001",
        index=1,
        start_position=2,
        end_position=6
    )

    # Test equality with identical message
    assert message == identical_msg

    # Test inequality with different message
    assert message != different_msg

    # Test inequality with a non-Message object
    assert message != "Not a message"
