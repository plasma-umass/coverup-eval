# file typesystem/base.py:85-94
# lines [85, 86, 87, 88, 89, 90, 91, 93, 94]
# branches ['88->89', '88->90', '90->91', '90->93']

import pytest
from typesystem.base import Message

@pytest.fixture
def message():
    class TestMessage(Message):
        def __init__(self, text, code, index=None, start_position=None, end_position=None):
            self.text = text
            self.code = code
            self.index = index
            self.start_position = start_position
            self.end_position = end_position if end_position is not None else start_position

    return TestMessage

def test_message_repr_no_index_no_position(message):
    msg = message("Sample text", "E001")
    expected_repr = "TestMessage(text='Sample text', code='E001')"
    assert repr(msg) == expected_repr

def test_message_repr_with_index_no_position(message):
    msg = message("Sample text", "E001", index=5)
    expected_repr = "TestMessage(text='Sample text', code='E001', index=5)"
    assert repr(msg) == expected_repr

def test_message_repr_with_start_position(message):
    msg = message("Sample text", "E001", start_position=10)
    expected_repr = "TestMessage(text='Sample text', code='E001', position=10)"
    assert repr(msg) == expected_repr

def test_message_repr_with_start_and_end_position(message):
    msg = message("Sample text", "E001", start_position=10, end_position=20)
    expected_repr = "TestMessage(text='Sample text', code='E001', start_position=10, end_position=20)"
    assert repr(msg) == expected_repr
