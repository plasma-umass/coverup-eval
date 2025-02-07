# file: pymonet/validation.py:74-83
# asked: {"lines": [74, 83], "branches": []}
# gained: {"lines": [74, 83], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_bind_success():
    # Arrange
    validation = Validation.success(10)
    
    # Act
    result = validation.bind(lambda x: Validation.success(x * 2))
    
    # Assert
    assert result == Validation.success(20)

def test_validation_bind_fail():
    # Arrange
    validation = Validation.fail(["error"])
    
    # Act
    result = validation.bind(lambda x: validation)
    
    # Assert
    assert result == validation  # Should remain the same since it's a failure

def test_validation_bind_function_called():
    # Arrange
    validation = Validation.success(10)
    def folder(value):
        return Validation.success(value + 5)
    
    # Act
    result = validation.bind(folder)
    
    # Assert
    assert result == Validation.success(15)
