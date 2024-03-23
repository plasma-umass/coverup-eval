# file pymonet/either.py:164-173
# lines [164, 173]
# branches []

import pytest
from pymonet.either import Right, Left

def test_right_bind_executes_mapper_function():
    def mapper(value):
        return Right(value * 2)

    right_value = Right(10)
    result = right_value.bind(mapper)

    assert isinstance(result, Right)
    assert result.value == 20

def test_right_bind_with_left_return():
    def mapper(value):
        return Left("Error")

    right_value = Right(10)
    result = right_value.bind(mapper)

    assert isinstance(result, Left)
    assert result.value == "Error"
