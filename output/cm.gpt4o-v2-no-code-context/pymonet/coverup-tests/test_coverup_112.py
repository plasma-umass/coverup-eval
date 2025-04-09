# file: pymonet/validation.py:146-155
# asked: {"lines": [153, 155], "branches": []}
# gained: {"lines": [153, 155], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

class TestValidation:
    def test_to_try_success(self, mocker):
        # Arrange
        validation = Validation(value="test_value", errors=[])
        mocker.patch.object(validation, 'is_success', return_value=True)
        
        # Act
        result = validation.to_try()
        
        # Assert
        assert isinstance(result, Try)
        assert result.is_success
        assert result.get() == "test_value"

    def test_to_try_failure(self, mocker):
        # Arrange
        validation = Validation(value="test_value", errors=["error"])
        mocker.patch.object(validation, 'is_success', return_value=False)
        
        # Act
        result = validation.to_try()
        
        # Assert
        assert isinstance(result, Try)
        assert not result.is_success
        assert result.get() == "test_value"
