# file: typesystem/base.py:29-70
# asked: {"lines": [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70], "branches": [[57, 58], [57, 61], [63, 64], [63, 67]]}
# gained: {"lines": [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70], "branches": [[57, 58], [57, 61], [63, 64], [63, 67]]}

import pytest
from typesystem.base import Message, Position

def test_message_with_all_parameters():
    position = Position(line_no=1, column_no=5, char_index=10)
    message = Message(
        text="Error message",
        code="error_code",
        key="username",
        index=None,
        position=position,
        start_position=None,
        end_position=None
    )
    assert message.text == "Error message"
    assert message.code == "error_code"
    assert message.index == ["username"]
    assert message.start_position == position
    assert message.end_position == position

def test_message_with_index():
    message = Message(
        text="Error message",
        code="error_code",
        key=None,
        index=["users", 3, "username"],
        position=None,
        start_position=None,
        end_position=None
    )
    assert message.text == "Error message"
    assert message.code == "error_code"
    assert message.index == ["users", 3, "username"]
    assert message.start_position is None
    assert message.end_position is None

def test_message_with_start_and_end_position():
    start_position = Position(line_no=1, column_no=5, char_index=10)
    end_position = Position(line_no=1, column_no=15, char_index=20)
    message = Message(
        text="Error message",
        code=None,
        key=None,
        index=None,
        position=None,
        start_position=start_position,
        end_position=end_position
    )
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == []
    assert message.start_position == start_position
    assert message.end_position == end_position

def test_message_with_default_code():
    message = Message(
        text="Error message",
        code=None,
        key=None,
        index=None,
        position=None,
        start_position=None,
        end_position=None
    )
    assert message.text == "Error message"
    assert message.code == "custom"
    assert message.index == []
    assert message.start_position is None
    assert message.end_position is None
