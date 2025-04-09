# file typesystem/base.py:201-204
# lines [204]
# branches ['202->204']

import pytest
from typesystem.base import BaseError
from typesystem.fields import Message

@pytest.fixture
def message():
    return Message(text="Error message", code="custom", index=["error_index"])

@pytest.fixture
def base_error_single_message(message):
    error = BaseError(messages=[message])
    return error

@pytest.fixture
def base_error_multiple_messages():
    error = BaseError(messages=[
        Message(text="First error", code="first_code", index=["first_index"]),
        Message(text="Second error", code="second_code", index=["second_index"])
    ])
    return error

def test_base_error_str_single_message_without_index():
    error = BaseError(text="Single error message")
    assert str(error) == "Single error message"

def test_base_error_str_single_message_with_index(base_error_single_message):
    assert str(base_error_single_message) == "{'error_index': 'Error message'}"

def test_base_error_str_multiple_messages(base_error_multiple_messages):
    assert str(base_error_multiple_messages) == "{'first_index': 'First error', 'second_index': 'Second error'}"
