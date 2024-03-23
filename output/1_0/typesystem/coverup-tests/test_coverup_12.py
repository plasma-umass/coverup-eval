# file typesystem/base.py:201-204
# lines [201, 202, 203, 204]
# branches ['202->203', '202->204']

import pytest
from typesystem.base import BaseError
from typesystem.fields import Message

@pytest.fixture
def message_without_index():
    return Message(text="Single error without index", index=None)

@pytest.fixture
def message_with_index():
    return Message(text="Error with index", index=[0])

@pytest.fixture
def base_error_single_message(message_without_index):
    error = BaseError(messages=[message_without_index])
    return error

@pytest.fixture
def base_error_multiple_messages(message_without_index, message_with_index):
    error = BaseError(messages=[message_without_index, message_with_index])
    return error

def test_base_error_str_single_message_without_index(base_error_single_message):
    assert str(base_error_single_message) == "Single error without index"

def test_base_error_str_multiple_messages(base_error_multiple_messages):
    assert str(base_error_multiple_messages) == str(dict(base_error_multiple_messages))
