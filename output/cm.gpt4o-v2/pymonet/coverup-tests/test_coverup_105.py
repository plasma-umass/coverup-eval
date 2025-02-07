# file: pymonet/monad_try.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_str():
    # Create instances of Try
    success_try = Try(value="Success", is_success=True)
    fail_try = Try(value="Failure", is_success=False)
    
    # Check the string representation
    assert str(success_try) == "Try[value=Success, is_success=True]"
    assert str(fail_try) == "Try[value=Failure, is_success=False]"
