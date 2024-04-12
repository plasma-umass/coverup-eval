# file pytutils/excs.py:4-15
# lines [4, 5, 9, 10, 11, 12, 13, 15]
# branches ['12->13', '12->15']

import pytest
from pytutils.excs import ok

def test_ok_passes_specified_exception():
    with ok(ValueError):
        raise ValueError("This should be passed")

def test_ok_reraises_unspecified_exception():
    with pytest.raises(KeyError):
        with ok(ValueError):
            raise KeyError("This should be reraised")

def test_ok_with_no_exceptions_passed():
    with pytest.raises(Exception) as exc_info:
        with ok():
            raise Exception("This should be reraised")
    assert str(exc_info.value) == "This should be reraised"

def test_ok_with_multiple_exceptions():
    with ok(ValueError, KeyError):
        raise ValueError("This should be passed")
    with ok(ValueError, KeyError):
        raise KeyError("This should be passed")
    with pytest.raises(IndexError):
        with ok(ValueError, KeyError):
            raise IndexError("This should be reraised")
