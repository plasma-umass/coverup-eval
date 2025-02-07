# file: pymonet/validation.py:33-43
# asked: {"lines": [33, 34, 43], "branches": []}
# gained: {"lines": [33, 34, 43], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_fail_with_default_error():
    result = Validation.fail()
    assert result.value is None
    assert result.errors == []

def test_validation_fail_with_specific_errors():
    errors = ["error1", "error2"]
    result = Validation.fail(errors)
    assert result.value is None
    assert result.errors == errors
