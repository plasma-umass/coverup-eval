# file typesystem/base.py:29-70
# lines [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70]
# branches ['57->58', '57->61', '63->64', '63->67']

import pytest
from typesystem.base import Message

class MockPosition:
    def __init__(self, line, column):
        self.line = line
        self.column = column

def test_message_initialization():
    # Test with only text
    msg = Message(text="Error message")
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

    # Test with text and code
    msg = Message(text="Error message", code="error_code")
    assert msg.text == "Error message"
    assert msg.code == "error_code"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

    # Test with key
    msg = Message(text="Error message", key="username")
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == ["username"]
    assert msg.start_position is None
    assert msg.end_position is None

    # Test with index
    msg = Message(text="Error message", index=["users", 3, "username"])
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == ["users", 3, "username"]
    assert msg.start_position is None
    assert msg.end_position is None

    # Test with position
    position = MockPosition(line=1, column=5)
    msg = Message(text="Error message", position=position)
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position == position
    assert msg.end_position == position

    # Test with start_position and end_position
    start_position = MockPosition(line=1, column=5)
    end_position = MockPosition(line=1, column=10)
    msg = Message(text="Error message", start_position=start_position, end_position=end_position)
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position == start_position
    assert msg.end_position == end_position

    # Test assertion error when both key and index are provided
    with pytest.raises(AssertionError):
        Message(text="Error message", key="username", index=["users", 3, "username"])

    # Test assertion error when both position and start_position/end_position are provided
    with pytest.raises(AssertionError):
        Message(text="Error message", position=position, start_position=start_position)

    with pytest.raises(AssertionError):
        Message(text="Error message", position=position, end_position=end_position)
