# file: typesystem/base.py:178-179
# asked: {"lines": [179], "branches": []}
# gained: {"lines": [179], "branches": []}

import pytest
from typesystem.base import BaseError, Message, Position

def test_baseerror_iter_single_message():
    position = Position(line_no=1, column_no=1, char_index=0)
    message = Message(text="Error message", code="error_code", key="key", position=position)
    error = BaseError(messages=[message])
    assert list(iter(error)) == ["key"]

def test_baseerror_iter_multiple_messages():
    position1 = Position(line_no=1, column_no=1, char_index=0)
    position2 = Position(line_no=2, column_no=2, char_index=10)
    message1 = Message(text="Error message 1", code="error_code_1", key="key1", position=position1)
    message2 = Message(text="Error message 2", code="error_code_2", key="key2", position=position2)
    error = BaseError(messages=[message1, message2])
    assert set(iter(error)) == {"key1", "key2"}
