# file: typesystem/base.py:194-199
# asked: {"lines": [194, 195, 196, 197, 198, 199], "branches": [[196, 197], [196, 199]]}
# gained: {"lines": [194, 195, 196, 197, 198, 199], "branches": [[196, 197], [196, 199]]}

import pytest
from typesystem.base import BaseError

class MockMessage:
    def __init__(self, text, code, index=None):
        self.text = text
        self.code = code
        self.index = index

    def __repr__(self):
        return f"MockMessage(text={self.text!r}, code={self.code!r}, index={self.index!r})"

class MockBaseError(BaseError):
    def __init__(self, messages):
        self._messages = messages

def test_base_error_repr_single_message_no_index():
    message = MockMessage(text="Error occurred", code="error_code")
    error = MockBaseError(messages=[message])
    expected_repr = "MockBaseError(text='Error occurred', code='error_code')"
    assert repr(error) == expected_repr

def test_base_error_repr_multiple_messages():
    message1 = MockMessage(text="First error", code="first_code")
    message2 = MockMessage(text="Second error", code="second_code", index=1)
    error = MockBaseError(messages=[message1, message2])
    expected_repr = "MockBaseError([MockMessage(text='First error', code='first_code', index=None), MockMessage(text='Second error', code='second_code', index=1)])"
    assert repr(error) == expected_repr
