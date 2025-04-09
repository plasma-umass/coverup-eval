# file pymonet/monad_try.py:66-77
# lines [66, 75, 76, 77]
# branches ['75->76', '75->77']

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        super().__init__(value, True)

class Failure(Try):
    def __init__(self, exception):
        super().__init__(exception, False)

def test_try_on_success_with_success(mocker):
    # Setup: Create a Success instance
    success_value = 42
    success_instance = Success(success_value)

    # Mock a success callback function
    success_callback = mocker.Mock()

    # Exercise: Call on_success on the Success instance
    result = success_instance.on_success(success_callback)

    # Verify: Check if the success_callback was called with the correct value
    success_callback.assert_called_once_with(success_value)

    # Verify: Check if the result is the same instance (for chaining)
    assert result is success_instance

def test_try_on_success_with_failure(mocker):
    # Setup: Create a Failure instance
    failure_instance = Failure(Exception("failure"))

    # Mock a success callback function
    success_callback = mocker.Mock()

    # Exercise: Call on_success on the Failure instance
    result = failure_instance.on_success(success_callback)

    # Verify: Check if the success_callback was not called
    success_callback.assert_not_called()

    # Verify: Check if the result is the same instance (for chaining)
    assert result is failure_instance
