# file: pymonet/monad_try.py:92-105
# asked: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from pymonet.monad_try import Try

def test_try_filter_success_true():
    # Arrange
    try_instance = Try(10, True)
    
    # Act
    result = try_instance.filter(lambda x: x > 5)
    
    # Assert
    assert result.is_success
    assert result.value == 10

def test_try_filter_success_false():
    # Arrange
    try_instance = Try(10, True)
    
    # Act
    result = try_instance.filter(lambda x: x < 5)
    
    # Assert
    assert not result.is_success
    assert result.value == 10

def test_try_filter_failure():
    # Arrange
    try_instance = Try(10, False)
    
    # Act
    result = try_instance.filter(lambda x: x > 5)
    
    # Assert
    assert not result.is_success
    assert result.value == 10
