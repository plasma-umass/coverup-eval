# file: pymonet/validation.py:63-72
# asked: {"lines": [72], "branches": []}
# gained: {"lines": [72], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_map():
    # Arrange
    validation = Validation("initial_value", ["error1", "error2"])
    mapper = lambda x: x.upper()

    # Act
    new_validation = validation.map(mapper)

    # Assert
    assert new_validation.value == "INITIAL_VALUE"
    assert new_validation.errors == ["error1", "error2"]

