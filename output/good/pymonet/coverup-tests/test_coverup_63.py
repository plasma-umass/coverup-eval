# file pymonet/lazy.py:151-160
# lines [151, 158, 160]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

def test_lazy_to_validation():
    # Setup a Lazy instance with a simple function
    lazy_value = Lazy(lambda: 42)

    # Call to_validation on the Lazy instance
    validation_result = lazy_value.to_validation()

    # Assert that the result is a Validation instance
    assert isinstance(validation_result, Validation)

    # Assert that the Validation instance is a success
    assert validation_result.is_success()

    # Assert that the value inside the Validation is the same as the Lazy value
    assert validation_result.value == 42
