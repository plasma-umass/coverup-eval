# file: pymonet/monad_try.py:10-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_success():
    try_instance = Try(value="Success", is_success=True)
    assert try_instance.value == "Success"
    assert try_instance.is_success is True

def test_try_failure():
    try_instance = Try(value="Failure", is_success=False)
    assert try_instance.value == "Failure"
    assert try_instance.is_success is False
