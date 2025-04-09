# file typesystem/base.py:190-192
# lines [191, 192]
# branches []

import pytest
from typesystem.base import BaseError

class MockBaseError(BaseError):
    def __init__(self, messages):
        self._messages = messages

def test_base_error_hash():
    # Create an instance of MockBaseError with mock messages
    mock_messages = ["error1", "error2"]
    error_instance = MockBaseError(mock_messages)
    
    # Call the __hash__ method and assert the result
    result = hash(error_instance)
    
    # Verify that the hash is computed correctly
    expected_ident = tuple(hash(m) for m in mock_messages)
    expected_hash = hash(expected_ident)
    assert result == expected_hash
