# file pymonet/monad_try.py:14-17
# lines [14, 15, 16, 17]
# branches []

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

def test_try_equality():
    success1 = Success(10)
    success2 = Success(10)
    success3 = Success(20)
    failure1 = Failure(10)
    failure2 = Failure(10)
    failure3 = Failure(20)

    # Test equality for Success instances
    assert success1 == success2
    assert success1 != success3
    assert success1 != failure1

    # Test equality for Failure instances
    assert failure1 == failure2
    assert failure1 != failure3
    assert failure1 != success1
