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
    def __init__(self, exception):
        self.value = exception
        self.is_success = False

def test_try_eq():
    # Create two Success instances with the same value
    success1 = Success(42)
    success2 = Success(42)
    # Create two Failure instances with the same exception
    exception = Exception("Error")
    failure1 = Failure(exception)
    failure2 = Failure(exception)
    # Create a Failure instance with a different exception
    failure3 = Failure(Exception("Different Error"))
    # Create a Success instance with a different value
    success3 = Success(43)

    # Test Success instances for equality
    assert success1 == success2
    assert success1 != success3
    assert success1 != failure1

    # Test Failure instances for equality
    assert failure1 == failure2
    assert failure1 != failure3
    assert failure1 != success1

    # Test against different types
    assert success1 != 42
    assert failure1 != "Error"
