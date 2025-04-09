# file: pymonet/validation.py:63-72
# asked: {"lines": [72], "branches": []}
# gained: {"lines": [72], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_map():
    # Arrange
    validation = Validation(value=10, errors=[])
    mapper = lambda x: x * 2

    # Act
    new_validation = validation.map(mapper)

    # Assert
    assert new_validation.value == 20
    assert new_validation.errors == []

def test_validation_map_with_errors():
    # Arrange
    validation = Validation(value=10, errors=['error1'])
    mapper = lambda x: x * 2

    # Act
    new_validation = validation.map(mapper)

    # Assert
    assert new_validation.value == 20
    assert new_validation.errors == ['error1']
