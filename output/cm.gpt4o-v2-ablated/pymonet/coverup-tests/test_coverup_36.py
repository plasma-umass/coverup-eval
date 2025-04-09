# file: pymonet/validation.py:21-31
# asked: {"lines": [21, 22, 31], "branches": []}
# gained: {"lines": [21, 22, 31], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_success_with_value():
    value = "test_value"
    validation = Validation.success(value)
    assert validation.value == value
    assert validation.errors == []

def test_validation_success_without_value():
    validation = Validation.success()
    assert validation.value is None
    assert validation.errors == []
