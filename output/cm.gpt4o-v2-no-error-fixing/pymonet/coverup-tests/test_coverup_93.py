# file: pymonet/monad_try.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_str():
    # Create a Try instance
    try_instance = Try(value="test_value", is_success=True)
    
    # Check the string representation
    assert str(try_instance) == "Try[value=test_value, is_success=True]"

    # Create another Try instance with different values
    try_instance_fail = Try(value="error_value", is_success=False)
    
    # Check the string representation
    assert str(try_instance_fail) == "Try[value=error_value, is_success=False]"
