# file typesystem/base.py:194-199
# lines [194, 195, 196, 197, 198, 199]
# branches ['196->197', '196->199']

import pytest
from typesystem.base import BaseError
from typesystem.fields import Message

@pytest.fixture
def single_message_error():
    message = Message(text="Error text", code="error_code")
    error = BaseError(messages=[message])
    yield error
    # No cleanup needed as no external resources are being used

@pytest.fixture
def indexed_message_error():
    message = Message(text="Error text", code="error_code", index=["error_index"])
    error = BaseError(messages=[message])
    yield error
    # No cleanup needed as no external resources are being used

def test_base_error_repr_single_message(single_message_error):
    expected_repr = "BaseError(text='Error text', code='error_code')"
    assert repr(single_message_error) == expected_repr

def test_base_error_repr_indexed_message(indexed_message_error):
    expected_repr = "BaseError([Message(text='Error text', code='error_code', index=['error_index'])])"
    assert repr(indexed_message_error) == expected_repr
