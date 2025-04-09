# file: pymonet/monad_try.py:116-128
# asked: {"lines": [126, 127, 128], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128], "branches": [[126, 127], [126, 128]]}

import pytest
from pymonet.monad_try import Try

def test_get_or_else_success():
    # Create a Try instance with is_success=True
    try_instance = Try(value="success_value", is_success=True)
    
    # Assert that get_or_else returns the value when is_success is True
    assert try_instance.get_or_else("default_value") == "success_value"

def test_get_or_else_failure():
    # Create a Try instance with is_success=False
    try_instance = Try(value="failure_value", is_success=False)
    
    # Assert that get_or_else returns the default value when is_success is False
    assert try_instance.get_or_else("default_value") == "default_value"
