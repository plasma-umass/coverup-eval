# file: typesystem/base.py:72-79
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest
from typesystem.base import Message

@pytest.fixture
def message_data():
    return {
        "text": "Error message",
        "code": "error_code",
        "index": [1, 2, 3],
        "position": None,
        "start_position": 5,
        "end_position": 10
    }

def test_message_equality(message_data):
    msg1 = Message(
        text=message_data["text"],
        code=message_data["code"],
        index=message_data["index"],
        position=message_data["position"],
        start_position=message_data["start_position"],
        end_position=message_data["end_position"]
    )
    
    msg2 = Message(
        text=message_data["text"],
        code=message_data["code"],
        index=message_data["index"],
        position=message_data["position"],
        start_position=message_data["start_position"],
        end_position=message_data["end_position"]
    )
    
    assert msg1 == msg2

def test_message_inequality(message_data):
    msg1 = Message(
        text=message_data["text"],
        code=message_data["code"],
        index=message_data["index"],
        position=message_data["position"],
        start_position=message_data["start_position"],
        end_position=message_data["end_position"]
    )
    
    msg2 = Message(
        text="Different message",
        code=message_data["code"],
        index=message_data["index"],
        position=message_data["position"],
        start_position=message_data["start_position"],
        end_position=message_data["end_position"]
    )
    
    assert msg1 != msg2

def test_message_equality_with_different_types(message_data):
    msg1 = Message(
        text=message_data["text"],
        code=message_data["code"],
        index=message_data["index"],
        position=message_data["position"],
        start_position=message_data["start_position"],
        end_position=message_data["end_position"]
    )
    
    assert msg1 != "Not a Message instance"
