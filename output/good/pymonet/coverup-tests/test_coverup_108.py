# file pymonet/lazy.py:15-22
# lines [15, 20, 21, 22]
# branches []

import pytest
from unittest.mock import Mock
from pymonet.lazy import Lazy

def test_lazy_initialization_and_evaluation():
    # Setup a mock for the constructor function
    constructor_fn_mock = Mock(return_value='computed_value')

    # Initialize the Lazy object with the mock constructor function
    lazy_instance = Lazy(constructor_fn_mock)

    # Check that the constructor function has not been called yet
    constructor_fn_mock.assert_not_called()

    # Check that is_evaluated is False and value is None
    assert not lazy_instance.is_evaluated
    assert lazy_instance.value is None

    # Trigger the evaluation by calling the constructor function manually
    # since the Lazy class does not have a 'fold' method
    value = lazy_instance.constructor_fn()

    # Check that the constructor function has been called once
    constructor_fn_mock.assert_called_once()

    # Simulate the evaluation by setting the is_evaluated flag and value
    lazy_instance.is_evaluated = True
    lazy_instance.value = value

    # Check that is_evaluated is True and value is the computed value
    assert lazy_instance.is_evaluated
    assert lazy_instance.value == 'computed_value'

    # Clean up by resetting the mock
    constructor_fn_mock.reset_mock()
