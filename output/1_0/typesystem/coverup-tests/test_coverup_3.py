# file typesystem/base.py:72-79
# lines [72, 73, 74, 75, 76, 77, 78]
# branches []

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    return Message(
        text="Test message",
        code="test_code",
        index=0,
        start_position=0,
        end_position=10
    )

def test_message_equality(message):
    # Create another message with the same properties
    same_message = Message(
        text="Test message",
        code="test_code",
        index=0,
        start_position=0,
        end_position=10
    )
    
    # Create a message with different properties
    different_message = Message(
        text="Different message",
        code="diff_code",
        index=1,
        start_position=10,
        end_position=20
    )
    
    # Test equality with the same message
    assert message == same_message
    
    # Test inequality with a different message
    assert message != different_message
    
    # Test inequality with a different type
    assert message != "not a message instance"
