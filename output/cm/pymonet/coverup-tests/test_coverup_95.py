# file pymonet/either.py:97-104
# lines [97, 104]
# branches []

import pytest
from pymonet.either import Left

def test_left_bind_does_not_call_mapper_function():
    left_value = Left('error')
    mapper_function_was_called = False

    def mapper_function(_):
        nonlocal mapper_function_was_called
        mapper_function_was_called = True
        return 'should not be called'

    result = left_value.bind(mapper_function)

    assert isinstance(result, Left), "Result should be an instance of Left"
    assert result.value == 'error', "Result should contain the original Left value"
    assert not mapper_function_was_called, "Mapper function should not be called"
