# file: typesystem/base.py:213-216
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

import pytest
from typesystem.base import ValidationError, BaseError, Message

def test_validation_error_inheritance():
    error = ValidationError(text="An error occurred")
    assert isinstance(error, BaseError)
    assert isinstance(error, Exception)

def test_validation_error_single_message():
    error = ValidationError(text="An error occurred", code="error_code", key="key")
    assert len(error._messages) == 1
    assert error._messages[0].text == "An error occurred"
    assert error._messages[0].code == "error_code"
    assert error._messages[0].index == ["key"]

def test_validation_error_multiple_messages():
    messages = [
        Message(text="Error 1"),
        Message(text="Error 2")
    ]
    error = ValidationError(messages=messages)
    assert len(error._messages) == 2
    assert error._messages[0].text == "Error 1"
    assert error._messages[1].text == "Error 2"

def test_validation_error_message_dict():
    error = ValidationError(text="An error occurred", key="key")
    assert error._message_dict["key"] == "An error occurred"

def test_validation_error_messages_method():
    error = ValidationError(text="An error occurred")
    messages = error.messages()
    assert len(messages) == 1
    assert messages[0].text == "An error occurred"

def test_validation_error_dict_like_access():
    error = ValidationError(text="An error occurred", key="key")
    assert error["key"] == "An error occurred"
    with pytest.raises(KeyError):
        _ = error["nonexistent_key"]

def test_validation_error_equality():
    error1 = ValidationError(text="An error occurred")
    error2 = ValidationError(text="An error occurred")
    assert error1 == error2

def test_validation_error_hash():
    error = ValidationError(text="An error occurred")
    assert isinstance(hash(error), int)

def test_validation_error_repr():
    error = ValidationError(text="An error occurred")
    assert repr(error) == "ValidationError(text='An error occurred', code='custom')"

def test_validation_error_str():
    error = ValidationError(text="An error occurred")
    assert str(error) == "An error occurred"
