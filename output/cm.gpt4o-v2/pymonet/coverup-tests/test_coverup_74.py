# file: pymonet/monad_try.py:10-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_init_success():
    value = "test_value"
    is_success = True
    try_instance = Try(value, is_success)
    assert try_instance.value == value
    assert try_instance.is_success == is_success

def test_try_init_failure():
    value = "test_value"
    is_success = False
    try_instance = Try(value, is_success)
    assert try_instance.value == value
    assert try_instance.is_success == is_success
