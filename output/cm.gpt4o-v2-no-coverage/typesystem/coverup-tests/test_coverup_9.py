# file: typesystem/base.py:85-94
# asked: {"lines": [85, 86, 87, 88, 89, 90, 91, 93, 94], "branches": [[88, 89], [88, 90], [90, 91], [90, 93]]}
# gained: {"lines": [85, 86, 87, 88, 89, 90, 91, 93, 94], "branches": [[88, 89], [88, 90], [90, 91], [90, 93]]}

import pytest
from typesystem.base import Message

def test_message_repr_no_index_no_position():
    message = Message(text="Error message", code="error_code")
    expected_repr = "Message(text='Error message', code='error_code')"
    assert repr(message) == expected_repr

def test_message_repr_with_index():
    message = Message(text="Error message", code="error_code", index=[1])
    expected_repr = "Message(text='Error message', code='error_code', index=[1])"
    assert repr(message) == expected_repr

def test_message_repr_with_start_position():
    position = (1, 2)
    message = Message(text="Error message", code="error_code", start_position=position, end_position=position)
    expected_repr = "Message(text='Error message', code='error_code', position=(1, 2))"
    assert repr(message) == expected_repr

def test_message_repr_with_different_positions():
    start_position = (1, 2)
    end_position = (3, 4)
    message = Message(text="Error message", code="error_code", start_position=start_position, end_position=end_position)
    expected_repr = "Message(text='Error message', code='error_code', start_position=(1, 2), end_position=(3, 4))"
    assert repr(message) == expected_repr

def test_message_repr_with_position():
    position = (1, 2)
    message = Message(text="Error message", code="error_code", position=position)
    expected_repr = "Message(text='Error message', code='error_code', position=(1, 2))"
    assert repr(message) == expected_repr
