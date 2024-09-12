# file: pytutils/excs.py:4-15
# asked: {"lines": [4, 5, 9, 10, 11, 12, 13, 15], "branches": [[12, 13], [12, 15]]}
# gained: {"lines": [4, 5, 9, 10, 11, 12, 13, 15], "branches": [[12, 13], [12, 15]]}

import pytest
from pytutils.excs import ok

def test_ok_no_exception():
    with ok():
        assert True  # No exception should be raised

def test_ok_catch_specified_exception():
    with ok(ValueError):
        raise ValueError("This should be caught")
    assert True  # If we reach here, the exception was caught

def test_ok_catch_multiple_exceptions():
    with ok(ValueError, KeyError):
        raise KeyError("This should be caught")
    assert True  # If we reach here, the exception was caught

def test_ok_raise_unexpected_exception():
    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError("This should not be caught")

def test_ok_no_exception_with_multiple():
    with ok(ValueError, KeyError):
        assert True  # No exception should be raised
