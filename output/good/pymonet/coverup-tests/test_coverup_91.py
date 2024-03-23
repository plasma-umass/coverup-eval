# file pymonet/validation.py:85-96
# lines [85, 96]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_ap_concats_errors():
    # Setup: Create a Validation instance with an initial value and error
    initial_validation = Validation('initial_value', ['initial_error'])

    # Define a function that returns a Validation with a new error
    def validation_fn(value):
        return Validation(value, ['new_error'])

    # Exercise: Apply the function to the initial Validation
    result_validation = initial_validation.ap(validation_fn)

    # Verify: Check if the result Validation has concatenated errors
    assert result_validation.errors == ['initial_error', 'new_error']

    # Cleanup: No cleanup required as no external state was modified
