# file typesystem/base.py:112-155
# lines [112, 115, 116, 117, 118, 119, 132, 134, 135, 138, 139, 140, 141, 142, 144, 145, 147, 150, 151, 152, 153, 154, 155]
# branches ['132->134', '132->138', '150->exit', '150->151', '152->153', '152->154']

import pytest
from unittest.mock import Mock
from typesystem.base import BaseError, Message, Position

def test_base_error_single_message():
    text = "Error message"
    code = "error_code"
    key = "error_key"
    position = Mock(spec=Position)
    
    error = BaseError(text=text, code=code, key=key, position=position)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == text
    assert error._messages[0].code == code
    assert error._messages[0].index == [key]
    assert error._message_dict == {key: text}

def test_base_error_multiple_messages():
    messages = [
        Message(text="First error", code="first_code", index=["first"]),
        Message(text="Second error", code="second_code", index=["second"]),
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 2
    assert error._messages[0].text == "First error"
    assert error._messages[1].text == "Second error"
    assert error._message_dict == {
        "first": "First error",
        "second": "Second error"
    }

def test_base_error_nested_messages():
    messages = [
        Message(text="Nested error", code="nested_code", index=["parent", "child"]),
    ]
    
    error = BaseError(messages=messages)
    
    assert len(error._messages) == 1
    assert error._messages[0].text == "Nested error"
    assert error._message_dict == {
        "parent": {
            "child": "Nested error"
        }
    }
