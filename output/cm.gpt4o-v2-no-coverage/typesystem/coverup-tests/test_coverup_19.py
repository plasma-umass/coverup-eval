# file: typesystem/base.py:29-70
# asked: {"lines": [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70], "branches": [[57, 58], [57, 61], [63, 64], [63, 67]]}
# gained: {"lines": [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70], "branches": [[57, 58], [57, 61], [63, 64], [63, 67]]}

import pytest
from typesystem.base import Message, Position

def test_message_with_code():
    msg = Message(text="Error message", code="error_code")
    assert msg.text == "Error message"
    assert msg.code == "error_code"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

def test_message_without_code():
    msg = Message(text="Error message")
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

def test_message_with_key():
    msg = Message(text="Error message", key="username")
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == ["username"]
    assert msg.start_position is None
    assert msg.end_position is None

def test_message_with_index():
    msg = Message(text="Error message", index=["users", 3, "username"])
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == ["users", 3, "username"]
    assert msg.start_position is None
    assert msg.end_position is None

def test_message_with_position():
    position = Position(line_no=1, column_no=5, char_index=10)
    msg = Message(text="Error message", position=position)
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position == position
    assert msg.end_position == position

def test_message_with_start_and_end_position():
    start_position = Position(line_no=1, column_no=5, char_index=10)
    end_position = Position(line_no=1, column_no=10, char_index=15)
    msg = Message(text="Error message", start_position=start_position, end_position=end_position)
    assert msg.text == "Error message"
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position == start_position
    assert msg.end_position == end_position

def test_message_with_key_and_index_raises_assertion_error():
    with pytest.raises(AssertionError):
        Message(text="Error message", key="username", index=["users", 3, "username"])

def test_message_with_position_and_start_end_position_raises_assertion_error():
    position = Position(line_no=1, column_no=5, char_index=10)
    with pytest.raises(AssertionError):
        Message(text="Error message", position=position, start_position=position, end_position=position)
