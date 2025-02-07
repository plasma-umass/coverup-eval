# file: typesystem/base.py:194-199
# asked: {"lines": [194, 195, 196, 197, 198, 199], "branches": [[196, 197], [196, 199]]}
# gained: {"lines": [194, 195, 196, 197, 198, 199], "branches": [[196, 197], [196, 199]]}

import pytest
from typesystem.base import BaseError, Message

def test_base_error_repr_single_message():
    message = Message(text="Error occurred", code="error_code", index=[])
    error = BaseError(messages=[message])
    expected_repr = "BaseError(text='Error occurred', code='error_code')"
    assert repr(error) == expected_repr

def test_base_error_repr_multiple_messages():
    message1 = Message(text="First error", code="first_code", index=[1])
    message2 = Message(text="Second error", code="second_code", index=[2])
    error = BaseError(messages=[message1, message2])
    expected_repr = f"BaseError([{message1!r}, {message2!r}])"
    assert repr(error) == expected_repr
