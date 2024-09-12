# file: pymonet/monad_try.py:14-17
# asked: {"lines": [14, 15, 16, 17], "branches": []}
# gained: {"lines": [14, 15, 16, 17], "branches": []}

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        self.value = value
        self.is_success = True

class Failure(Try):
    def __init__(self, value):
        self.value = value
        self.is_success = False

def test_try_eq_success():
    success1 = Success(10)
    success2 = Success(10)
    assert success1 == success2

def test_try_eq_failure():
    failure1 = Failure(10)
    failure2 = Failure(10)
    assert failure1 == failure2

def test_try_eq_different_types():
    success = Success(10)
    failure = Failure(10)
    assert success != failure

def test_try_eq_different_values():
    success1 = Success(10)
    success2 = Success(20)
    assert success1 != success2

def test_try_eq_different_is_success():
    success = Success(10)
    failure = Failure(10)
    assert success != failure
