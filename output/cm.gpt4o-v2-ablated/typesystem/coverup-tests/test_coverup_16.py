# file: typesystem/base.py:72-79
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest

from typesystem.base import Message

@pytest.fixture
def message():
    return Message(
        text="Sample text",
        code="E001",
        index=0,
        start_position=0,
        end_position=10
    )

def test_message_equality_same_object(message):
    assert message == message

def test_message_equality_identical_object(message):
    other_message = Message(
        text="Sample text",
        code="E001",
        index=0,
        start_position=0,
        end_position=10
    )
    assert message == other_message

def test_message_equality_different_text(message):
    other_message = Message(
        text="Different text",
        code="E001",
        index=0,
        start_position=0,
        end_position=10
    )
    assert message != other_message

def test_message_equality_different_code(message):
    other_message = Message(
        text="Sample text",
        code="E002",
        index=0,
        start_position=0,
        end_position=10
    )
    assert message != other_message

def test_message_equality_different_index(message):
    other_message = Message(
        text="Sample text",
        code="E001",
        index=1,
        start_position=0,
        end_position=10
    )
    assert message != other_message

def test_message_equality_different_start_position(message):
    other_message = Message(
        text="Sample text",
        code="E001",
        index=0,
        start_position=1,
        end_position=10
    )
    assert message != other_message

def test_message_equality_different_end_position(message):
    other_message = Message(
        text="Sample text",
        code="E001",
        index=0,
        start_position=0,
        end_position=11
    )
    assert message != other_message

def test_message_equality_different_type(message):
    assert message != "Not a Message object"
