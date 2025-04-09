# file: pymonet/either.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.either import Either, Right, Left

class TestEither:
    def test_ap_with_right(self):
        # Create a Right instance with a function
        right_func = Right(lambda x: x + 1)
        # Create a Right instance with a value
        right_value = Right(1)
        # Apply the function inside right_func to right_value
        result = right_func.ap(right_value)
        # Assert the result is a Right instance with the expected value
        assert result.is_right()
        assert result.value == 2

    def test_ap_with_left(self):
        # Create a Left instance with an error message
        left_func = Left("error")
        # Create a Right instance with a value
        right_value = Right(1)
        # Apply the function inside left_func to right_value
        result = right_value.ap(left_func)
        # Assert the result is a Left instance with the same error message
        assert result.is_left()
        assert result.value == "error"

    def test_ap_with_right_and_left_value(self):
        # Create a Right instance with a function
        right_func = Right(lambda x: x + 1)
        # Create a Left instance with an error message
        left_value = Left("error")
        # Apply the function inside right_func to left_value
        result = left_value.ap(right_func)
        # Assert the result is a Left instance with the same error message
        assert result.is_left()
        assert result.value == "error"
