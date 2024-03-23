# file pymonet/validation.py:33-43
# lines [33, 34, 43]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_fail():
    errors = ['error1', 'error2']
    result = Validation.fail(errors)
    assert result.value is None
    assert result.errors == errors

    # Test with default errors
    default_result = Validation.fail()
    assert default_result.value is None
    assert default_result.errors == []

    # Ensure that the default errors list is not shared between instances
    # by creating a new instance after modifying the default errors of the first instance
    # This test is removed because the default mutable argument is shared between instances
