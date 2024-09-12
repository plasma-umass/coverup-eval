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
    message = Message(text="Error message", code="error_code", index=[1, 2, 3])
    expected_repr = "Message(text='Error message', code='error_code', index=[1, 2, 3])"
    assert repr(message) == expected_repr

def test_message_repr_with_start_position():
    message = Message(text="Error message", code="error_code", start_position=5, end_position=5)
    expected_repr = "Message(text='Error message', code='error_code', position=5)"
    assert repr(message) == expected_repr

def test_message_repr_with_start_and_end_position():
    message = Message(text="Error message", code="error_code", start_position=5, end_position=10)
    expected_repr = "Message(text='Error message', code='error_code', start_position=5, end_position=10)"
    assert repr(message) == expected_repr

def test_message_repr_with_none_position():
    message = Message(text="Error message", code="error_code", start_position=None, end_position=None)
    expected_repr = "Message(text='Error message', code='error_code')"
    assert repr(message) == expected_repr
