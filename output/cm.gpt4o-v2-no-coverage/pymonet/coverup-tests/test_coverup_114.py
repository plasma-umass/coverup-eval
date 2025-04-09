# file: pymonet/validation.py:74-83
# asked: {"lines": [74, 83], "branches": []}
# gained: {"lines": [74, 83], "branches": []}

import pytest
from pymonet.validation import Validation

def test_validation_bind_success():
    # Arrange
    validation = Validation.success(10)
    folder = lambda x: Validation.success(x * 2)
    
    # Act
    result = validation.bind(folder)
    
    # Assert
    assert result == Validation.success(20)

def test_validation_bind_fail():
    # Arrange
    validation = Validation.fail(["error"])
    folder = lambda x: Validation.fail(["error"])
    
    # Act
    result = validation.bind(folder)
    
    # Assert
    assert result == Validation.fail(["error"])
