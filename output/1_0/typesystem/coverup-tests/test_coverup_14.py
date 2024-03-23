# file typesystem/base.py:157-176
# lines [157, 158, 167, 168, 169, 170, 171, 172, 174, 176]
# branches ['167->168', '167->176']

import pytest
from typesystem.base import BaseError, Message

class CustomError(BaseError):
    def __init__(self, messages):
        self._messages = messages

@pytest.fixture
def error_messages():
    return [
        Message(text="Error 1", code="code1", index=["field1"]),
        Message(text="Error 2", code="code2", index=["field2"]),
    ]

def test_base_error_messages_with_prefix(error_messages):
    error = CustomError(error_messages)
    prefixed_messages = error.messages(add_prefix="prefix")
    assert len(prefixed_messages) == 2
    assert prefixed_messages[0].text == "Error 1"
    assert prefixed_messages[0].code == "code1"
    assert prefixed_messages[0].index == ["prefix", "field1"]
    assert prefixed_messages[1].text == "Error 2"
    assert prefixed_messages[1].code == "code2"
    assert prefixed_messages[1].index == ["prefix", "field2"]

def test_base_error_messages_without_prefix(error_messages):
    error = CustomError(error_messages)
    non_prefixed_messages = error.messages()
    assert non_prefixed_messages == error_messages
