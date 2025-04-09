# file: pymonet/validation.py:85-96
# asked: {"lines": [85, 96], "branches": []}
# gained: {"lines": [85, 96], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_ap_success(self):
        # Arrange
        validation = Validation(10, [])
        def fn(value):
            return Validation(value * 2, [])
        
        # Act
        result = validation.ap(fn)
        
        # Assert
        assert result.value == 10
        assert result.errors == []

    def test_ap_with_errors(self):
        # Arrange
        validation = Validation(10, ['initial error'])
        def fn(value):
            return Validation(value * 2, ['new error'])
        
        # Act
        result = validation.ap(fn)
        
        # Assert
        assert result.value == 10
        assert result.errors == ['initial error', 'new error']
