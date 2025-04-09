# file: pymonet/validation.py:63-72
# asked: {"lines": [63, 72], "branches": []}
# gained: {"lines": [63, 72], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_map_success(self):
        # Arrange
        validation = Validation(value=10, errors=[])
        mapper = lambda x: x * 2

        # Act
        new_validation = validation.map(mapper)

        # Assert
        assert new_validation.value == 20
        assert new_validation.errors == []

    def test_map_with_errors(self):
        # Arrange
        validation = Validation(value=10, errors=['error1'])
        mapper = lambda x: x * 2

        # Act
        new_validation = validation.map(mapper)

        # Assert
        assert new_validation.value == 20
        assert new_validation.errors == ['error1']

    def test_map_with_complex_mapper(self):
        # Arrange
        validation = Validation(value=5, errors=['error1', 'error2'])
        mapper = lambda x: x ** 2

        # Act
        new_validation = validation.map(mapper)

        # Assert
        assert new_validation.value == 25
        assert new_validation.errors == ['error1', 'error2']
