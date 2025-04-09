# file pymonet/either.py:59-68
# lines [59, 66, 68]
# branches []

import pytest
from pymonet.either import Either
from pymonet.monad_try import Try

class Right(Either):
    def __init__(self, value):
        self.value = value

    def is_right(self):
        return True

class Left(Either):
    def __init__(self, value):
        self.value = value

    def is_right(self):
        return False

def test_either_to_try():
    # Test the to_try method with a Right instance
    right_value = 42
    right_either = Right(right_value)
    right_try = right_either.to_try()
    assert isinstance(right_try, Try)
    assert right_try.is_success == True
    assert right_try.get_or_else(None) == right_value

    # Test the to_try method with a Left instance
    left_value = "error"
    left_either = Left(left_value)
    left_try = left_either.to_try()
    assert isinstance(left_try, Try)
    assert left_try.is_success == False
    assert left_try.get_or_else(None) != left_value
