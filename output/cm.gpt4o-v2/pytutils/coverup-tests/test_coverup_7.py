# file: pytutils/excs.py:4-15
# asked: {"lines": [4, 5, 9, 10, 11, 12, 13, 15], "branches": [[12, 13], [12, 15]]}
# gained: {"lines": [4, 5, 9, 10, 11, 12, 13, 15], "branches": [[12, 13], [12, 15]]}

import pytest
from pytutils.excs import ok

def test_ok_no_exception():
    with ok():
        pass  # No exception should be raised

def test_ok_pass_exception():
    with ok(ValueError):
        raise ValueError("This should pass")

def test_ok_raise_exception():
    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError("This should not pass")
