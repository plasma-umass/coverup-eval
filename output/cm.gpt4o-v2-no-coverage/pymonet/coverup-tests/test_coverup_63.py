# file: pymonet/validation.py:33-43
# asked: {"lines": [33, 34, 43], "branches": []}
# gained: {"lines": [33, 34, 43], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_fail():
    # Test with default errors
    v = Validation.fail()
    assert v.value is None
    assert v.errors == []

    # Test with specific errors
    errors = ["error1", "error2"]
    v = Validation.fail(errors)
    assert v.value is None
    assert v.errors == errors

    # Clean up
    del v
    del errors
