# file: typesystem/base.py:178-179
# asked: {"lines": [178, 179], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from typesystem.base import BaseError

class MockMessage:
    def __init__(self, text, code, key):
        self.text = text
        self.code = code
        self.index = [key]

def test_baseerror_iter():
    # Create a sample message
    message = MockMessage(text="Sample error", code="error_code", key="key")
    
    # Instantiate BaseError with the sample message
    error = BaseError(messages=[message])
    
    # Convert the iterator to a list to force iteration
    keys = list(iter(error))
    
    # Assert that the keys are as expected
    assert keys == ["key"]

    # Clean up
    del error
    del message
