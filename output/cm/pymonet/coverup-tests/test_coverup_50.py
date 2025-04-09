# file pymonet/validation.py:8-14
# lines [8, 12, 13, 14]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_eq():
    # Create two Validation instances with the same value and errors
    validation1 = Validation('test_value', ['error1', 'error2'])
    validation2 = Validation('test_value', ['error1', 'error2'])

    # Create a third Validation instance with different value and errors
    validation3 = Validation('different_value', ['error3'])

    # Create a non-Validation instance
    non_validation = "I am not a Validation instance"

    # Test __eq__ for equal Validations
    assert validation1 == validation2, "Validation instances with same value and errors should be equal"

    # Test __eq__ for different Validations
    assert not (validation1 == validation3), "Validation instances with different value or errors should not be equal"

    # Test __eq__ with non-Validation instance
    assert not (validation1 == non_validation), "Validation instance should not be equal to non-Validation instance"
