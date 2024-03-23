# file typesystem/base.py:29-70
# lines [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70]
# branches ['57->58', '57->61', '63->64', '63->67']

import pytest
from typesystem.base import Message

class MockPosition:
    def __init__(self, line=None, column=None):
        self.line = line
        self.column = column

def test_message_initialization():
    # Test initialization with position only
    position = MockPosition(line=1, column=1)
    message = Message(text="Error message", position=position)
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == []
    assert message.start_position == position
    assert message.end_position == position

    # Test initialization with start_position and end_position
    start_position = MockPosition(line=1, column=1)
    end_position = MockPosition(line=1, column=5)
    message = Message(text="Error message", start_position=start_position, end_position=end_position)
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == []
    assert message.start_position == start_position
    assert message.end_position == end_position

    # Test initialization with key
    message = Message(text="Error message", key="username")
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == ["username"]

    # Test initialization with index
    message = Message(text="Error message", index=['users', 3, 'username'])
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == ['users', 3, 'username']

    # Test initialization with code
    message = Message(text="Error message", code="max_length")
    assert message.text == "Error message"
    assert message.code == "max_length"
    assert message.index == []

    # Test assertion error when both key and index are provided
    with pytest.raises(AssertionError):
        Message(text="Error message", key="username", index=['users', 3, 'username'])

    # Test assertion error when both position and start_position are provided
    with pytest.raises(AssertionError):
        Message(text="Error message", position=position, start_position=start_position)

    # Test assertion error when both position and end_position are provided
    with pytest.raises(AssertionError):
        Message(text="Error message", position=position, end_position=end_position)
