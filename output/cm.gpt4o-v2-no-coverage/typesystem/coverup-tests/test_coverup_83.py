# file: typesystem/base.py:112-155
# asked: {"lines": [153], "branches": [[152, 153]]}
# gained: {"lines": [153], "branches": [[152, 153]]}

import pytest
from typesystem.base import BaseError, Message, Position

def test_base_error_single_message():
    text = "Error message"
    code = "error_code"
    key = "error_key"
    position = Position(1, 2, 3)
    
    error = BaseError(text=text, code=code, key=key, position=position)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == text
    assert error._messages[0].code == code
    assert error._messages[0].index == [key]
    assert error._messages[0].start_position == position
    assert error._messages[0].end_position == position
    assert error._message_dict[key] == text

def test_base_error_multiple_messages():
    messages = [
        Message(text="Error 1", code="code1", key="key1"),
        Message(text="Error 2", code="code2", key="key2")
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 2
    assert error._messages[0].text == "Error 1"
    assert error._messages[1].text == "Error 2"
    assert error._message_dict["key1"] == "Error 1"
    assert error._message_dict["key2"] == "Error 2"

def test_base_error_message_dict_nested():
    messages = [
        Message(text="Nested error", index=["level1", "level2"])
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == "Nested error"
    assert error._message_dict["level1"]["level2"] == "Nested error"
