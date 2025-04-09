# file: typesystem/base.py:85-94
# asked: {"lines": [90, 91, 93], "branches": [[88, 90], [90, 91], [90, 93]]}
# gained: {"lines": [90, 91, 93], "branches": [[88, 90], [90, 91], [90, 93]]}

import pytest
from typesystem.base import Message

def test_message_repr_no_position():
    message = Message(text="Error message", code="error_code")
    expected_repr = "Message(text='Error message', code='error_code')"
    assert repr(message) == expected_repr

def test_message_repr_same_start_end_position():
    position = "pos"
    message = Message(text="Error message", code="error_code", start_position=position, end_position=position)
    expected_repr = "Message(text='Error message', code='error_code', position='pos')"
    assert repr(message) == expected_repr

def test_message_repr_different_start_end_position():
    start_position = "start_pos"
    end_position = "end_pos"
    message = Message(text="Error message", code="error_code", start_position=start_position, end_position=end_position)
    expected_repr = "Message(text='Error message', code='error_code', start_position='start_pos', end_position='end_pos')"
    assert repr(message) == expected_repr
