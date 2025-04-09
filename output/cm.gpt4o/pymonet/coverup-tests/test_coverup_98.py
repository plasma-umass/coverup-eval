# file pymonet/validation.py:1-3
# lines [1, 2]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_class():
    # Test instantiation of the Validation class with required arguments
    validation_instance = Validation(value="success", errors=[])
    assert isinstance(validation_instance, Validation)

    # Test the docstring of the Validation class
    assert validation_instance.__doc__ == "It that can hold either a success value or a failure value and has methods for accumulating errors"
