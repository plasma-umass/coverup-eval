# file typesystem/base.py:85-94
# lines [85, 86, 87, 88, 89, 90, 91, 93, 94]
# branches ['88->89', '88->90', '90->91', '90->93']

import pytest

from typesystem.base import Message

@pytest.fixture
def message():
    return Message(text="Error text", code="error_code")

def test_message_repr_without_index_and_position(message):
    expected_repr = "Message(text='Error text', code='error_code')"
    assert repr(message) == expected_repr

def test_message_repr_with_index(message):
    message.index = 1
    expected_repr = "Message(text='Error text', code='error_code', index=1)"
    assert repr(message) == expected_repr

def test_message_repr_with_same_start_and_end_position(message):
    message.start_position = 5
    message.end_position = 5
    expected_repr = "Message(text='Error text', code='error_code', position=5)"
    assert repr(message) == expected_repr

def test_message_repr_with_different_start_and_end_position(message):
    message.start_position = 5
    message.end_position = 10
    expected_repr = "Message(text='Error text', code='error_code', start_position=5, end_position=10)"
    assert repr(message) == expected_repr
