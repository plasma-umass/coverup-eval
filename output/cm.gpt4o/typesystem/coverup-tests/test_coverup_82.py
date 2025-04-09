# file typesystem/base.py:81-83
# lines [82, 83]
# branches []

import pytest
from typesystem.base import Message

def test_message_hash(mocker):
    # Mocking the attributes 'code' and 'index' to ensure lines 82-83 are executed
    message = Message(text="test_text")
    mocker.patch.object(message, 'code', 'test_code')
    mocker.patch.object(message, 'index', [1, 2, 3])

    # Calculate the hash to trigger the __hash__ method
    result = hash(message)

    # Verify that the hash is computed correctly
    expected_ident = ('test_code', (1, 2, 3))
    expected_hash = hash(expected_ident)
    assert result == expected_hash
