# file: pymonet/monad_try.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_str():
    # Test the __str__ method for a successful Try
    success_try = Try(value="success", is_success=True)
    assert str(success_try) == "Try[value=success, is_success=True]"

    # Test the __str__ method for a failed Try
    fail_try = Try(value="failure", is_success=False)
    assert str(fail_try) == "Try[value=failure, is_success=False]"
