# file pytutils/excs.py:4-15
# lines [4, 5, 9, 10, 11, 12, 13, 15]
# branches ['12->13', '12->15']

import pytest
from pytutils.excs import ok

def test_ok_context_manager_pass_exception():
    with ok(ValueError):
        raise ValueError("This should be passed")

def test_ok_context_manager_raise_exception():
    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError("This should be raised")

def test_ok_context_manager_no_exception():
    with ok(ValueError):
        pass  # No exception should be raised here
