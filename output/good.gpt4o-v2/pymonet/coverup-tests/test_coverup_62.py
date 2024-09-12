# file: pymonet/validation.py:21-31
# asked: {"lines": [21, 22, 31], "branches": []}
# gained: {"lines": [21, 22, 31], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_success_with_value():
    result = Validation.success("test_value")
    assert isinstance(result, Validation)
    assert result.value == "test_value"
    assert result.errors == []

def test_validation_success_without_value():
    result = Validation.success()
    assert isinstance(result, Validation)
    assert result.value is None
    assert result.errors == []
