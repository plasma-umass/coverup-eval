# file: typesystem/base.py:184-185
# asked: {"lines": [184, 185], "branches": []}
# gained: {"lines": [184, 185], "branches": []}

import pytest
from typesystem.base import BaseError
from typesystem.base import Message

def test_base_error_getitem():
    # Create a mock message
    message = Message(text="Error message", code="error_code", key="key", position=None)
    
    # Initialize BaseError with the mock message
    error = BaseError(messages=[message])
    
    # Test __getitem__ method
    assert error["key"] == "Error message"
    
    # Clean up
    del error
