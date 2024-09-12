# file: pymonet/monad_try.py:40-51
# asked: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}
# gained: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}

import pytest
from pymonet.monad_try import Try

def test_try_map_success():
    # Arrange
    success_try = Try(10, True)
    
    # Act
    result = success_try.map(lambda x: x + 5)
    
    # Assert
    assert result.is_success
    assert result.value == 15

def test_try_map_failure():
    # Arrange
    failure_try = Try("error", False)
    
    # Act
    result = failure_try.map(lambda x: x + 5)
    
    # Assert
    assert not result.is_success
    assert result.value == "error"
