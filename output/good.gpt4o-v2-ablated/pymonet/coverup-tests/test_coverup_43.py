# file: pymonet/validation.py:33-43
# asked: {"lines": [33, 34, 43], "branches": []}
# gained: {"lines": [33, 34, 43], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_fail_with_no_errors():
    validation = Validation.fail()
    assert validation.value is None
    assert validation.errors == []

def test_validation_fail_with_errors():
    errors = ["error1", "error2"]
    validation = Validation.fail(errors)
    assert validation.value is None
    assert validation.errors == errors
