# file: pymonet/validation.py:85-96
# asked: {"lines": [85, 96], "branches": []}
# gained: {"lines": [85, 96], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_ap_success():
    # Arrange
    validation = Validation(10, ["initial error"])
    def fn(value):
        return Validation(value * 2, ["new error"])

    # Act
    result = validation.ap(fn)

    # Assert
    assert result.value == 10
    assert result.errors == ["initial error", "new error"]

def test_validation_ap_fail():
    # Arrange
    validation = Validation(None, ["initial error"])
    def fn(value):
        return Validation(None, ["new error"])

    # Act
    result = validation.ap(fn)

    # Assert
    assert result.value is None
    assert result.errors == ["initial error", "new error"]
