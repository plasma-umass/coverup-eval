# file: pymonet/monad_try.py:79-90
# asked: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}
# gained: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}

import pytest
from pymonet.monad_try import Try

def test_on_fail_success():
    # Create a Try instance with is_success=True
    try_instance = Try(value="Success", is_success=True)
    
    # Define a fail callback that should not be called
    def fail_callback(value):
        assert False, "Fail callback should not be called"
    
    # Call on_fail and assert the return value is the same instance
    result = try_instance.on_fail(fail_callback)
    assert result is try_instance

def test_on_fail_failure():
    # Create a Try instance with is_success=False
    try_instance = Try(value="Failure", is_success=False)
    
    # Define a fail callback that should be called
    def fail_callback(value):
        assert value == "Failure"
    
    # Call on_fail and assert the return value is the same instance
    result = try_instance.on_fail(fail_callback)
    assert result is try_instance
