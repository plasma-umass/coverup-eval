# file: typesystem/base.py:112-155
# asked: {"lines": [112, 115, 116, 117, 118, 119, 132, 134, 135, 138, 139, 140, 141, 142, 144, 145, 147, 150, 151, 152, 153, 154, 155], "branches": [[132, 134], [132, 138], [150, 0], [150, 151], [152, 153], [152, 154]]}
# gained: {"lines": [112, 115, 116, 117, 118, 119, 132, 134, 135, 138, 139, 140, 141, 142, 144, 145, 147, 150, 151, 152, 153, 154, 155], "branches": [[132, 134], [132, 138], [150, 0], [150, 151], [152, 153], [152, 154]]}

import pytest
from typesystem.base import BaseError, Message, Position

def test_base_error_single_message():
    text = "Error message"
    code = "error_code"
    key = "error_key"
    position = Position(line_no=1, column_no=2, char_index=3)
    
    error = BaseError(text=text, code=code, key=key, position=position)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == text
    assert error._messages[0].code == code
    assert error._messages[0].index == [key]
    assert error._messages[0].start_position == position
    assert error._messages[0].end_position == position
    assert error._message_dict == {key: text}

def test_base_error_multiple_messages():
    messages = [
        Message(text="Error 1", code="code1", key="key1"),
        Message(text="Error 2", code="code2", key="key2")
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 2
    assert error._messages[0].text == "Error 1"
    assert error._messages[1].text == "Error 2"
    assert error._message_dict == {"key1": "Error 1", "key2": "Error 2"}

def test_base_error_nested_message_dict():
    messages = [
        Message(text="Nested error", code="nested_code", index=["parent", "child"])
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == "Nested error"
    assert error._message_dict == {"parent": {"child": "Nested error"}}
