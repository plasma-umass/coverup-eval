# file: pymonet/monad_try.py:107-114
# asked: {"lines": [107, 114], "branches": []}
# gained: {"lines": [107, 114], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_get():
    # Create an instance of Try with a value
    value = 42
    try_instance = Try(value, True)
    
    # Assert that the get method returns the correct value
    assert try_instance.get() == value

    # Clean up
    del try_instance
