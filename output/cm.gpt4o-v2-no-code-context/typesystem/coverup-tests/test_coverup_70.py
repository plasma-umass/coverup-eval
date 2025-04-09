# file: typesystem/base.py:29-70
# asked: {"lines": [58, 59, 67, 68, 69, 70], "branches": [[57, 58], [63, 67]]}
# gained: {"lines": [58, 59, 67, 68, 69, 70], "branches": [[57, 58], [63, 67]]}

import pytest
from typesystem.base import Message, Position

def test_message_with_key_and_no_index():
    message = Message(text="Test message", key="username")
    assert message.text == "Test message"
    assert message.code == "custom"
    assert message.index == ["username"]

def test_message_with_position_and_no_start_end_position():
    position = Position(1, 5, 10)  # Assuming Position takes line, column, and char_index as positional arguments
    message = Message(text="Test message", position=position)
    assert message.text == "Test message"
    assert message.code == "custom"
    assert message.start_position == position
    assert message.end_position == position

def test_message_with_start_end_position_and_no_position():
    start_position = Position(1, 5, 10)  # Assuming Position takes line, column, and char_index as positional arguments
    end_position = Position(1, 10, 15)  # Assuming Position takes line, column, and char_index as positional arguments
    message = Message(text="Test message", start_position=start_position, end_position=end_position)
    assert message.text == "Test message"
    assert message.code == "custom"
    assert message.start_position == start_position
    assert message.end_position == end_position

def test_message_with_key_and_index_raises_assertion_error():
    with pytest.raises(AssertionError):
        Message(text="Test message", key="username", index=["users", 3, "username"])

def test_message_with_position_and_start_position_raises_assertion_error():
    position = Position(1, 5, 10)  # Assuming Position takes line, column, and char_index as positional arguments
    start_position = Position(1, 5, 10)  # Assuming Position takes line, column, and char_index as positional arguments
    with pytest.raises(AssertionError):
        Message(text="Test message", position=position, start_position=start_position)

def test_message_with_position_and_end_position_raises_assertion_error():
    position = Position(1, 5, 10)  # Assuming Position takes line, column, and char_index as positional arguments
    end_position = Position(1, 10, 15)  # Assuming Position takes line, column, and char_index as positional arguments
    with pytest.raises(AssertionError):
        Message(text="Test message", position=position, end_position=end_position)
