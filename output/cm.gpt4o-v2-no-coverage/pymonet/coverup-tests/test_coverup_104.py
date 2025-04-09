# file: pymonet/validation.py:85-96
# asked: {"lines": [85, 96], "branches": []}
# gained: {"lines": [85, 96], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_ap_success():
    # Arrange
    validation = Validation("value", ["error1"])
    fn = lambda x: Validation(x, ["error2"])

    # Act
    result = validation.ap(fn)

    # Assert
    assert result.value == "value"
    assert result.errors == ["error1", "error2"]

def test_validation_ap_fail():
    # Arrange
    validation = Validation("value", ["error1"])
    fn = lambda x: Validation(x, ["error2", "error3"])

    # Act
    result = validation.ap(fn)

    # Assert
    assert result.value == "value"
    assert result.errors == ["error1", "error2", "error3"]
