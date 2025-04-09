# file: pymonet/validation.py:74-83
# asked: {"lines": [74, 83], "branches": []}
# gained: {"lines": [74, 83], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_bind_success(self):
        # Arrange
        validation = Validation(42, None)

        def folder(value):
            return value * 2

        # Act
        result = validation.bind(folder)

        # Assert
        assert result == 84

    def test_bind_failure(self):
        # Arrange
        validation = Validation(None, "Some error")

        def folder(value):
            if value is None:
                return "Error"
            return value * 2

        # Act
        result = validation.bind(folder)

        # Assert
        assert result == "Error"
