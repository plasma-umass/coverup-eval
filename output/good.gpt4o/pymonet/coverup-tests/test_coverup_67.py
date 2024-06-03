# file pymonet/validation.py:33-43
# lines [33, 34, 43]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_fail():
    # Call the fail method with a specific error list
    errors = ['error1', 'error2']
    result = Validation.fail(errors)
    
    # Assert that the result is an instance of Validation
    assert isinstance(result, Validation)
    
    # Assert that the result has the correct attributes
    assert result.value is None
    assert result.errors == errors
