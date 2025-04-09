# file: pymonet/validation.py:63-72
# asked: {"lines": [63, 72], "branches": []}
# gained: {"lines": [63, 72], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_map():
    # Arrange
    validation = Validation(10, ["error1"])
    mapper = lambda x: x * 2

    # Act
    new_validation = validation.map(mapper)

    # Assert
    assert new_validation.value == 20
    assert new_validation.errors == ["error1"]

    # Clean up
    del validation
    del new_validation
    del mapper
