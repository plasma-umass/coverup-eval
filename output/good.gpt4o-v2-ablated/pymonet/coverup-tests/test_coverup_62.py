# file: pymonet/validation.py:85-96
# asked: {"lines": [85, 96], "branches": []}
# gained: {"lines": [85, 96], "branches": []}

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_ap_success(self):
        # Arrange
        validation = Validation(10, [])
        fn = lambda x: Validation(x + 5, [])
        
        # Act
        result = validation.ap(fn)
        
        # Assert
        assert result.value == 10
        assert result.errors == []

    def test_ap_with_errors(self):
        # Arrange
        validation = Validation(10, ['error1'])
        fn = lambda x: Validation(x + 5, ['error2'])
        
        # Act
        result = validation.ap(fn)
        
        # Assert
        assert result.value == 10
        assert result.errors == ['error1', 'error2']
