# file: pymonet/monad_try.py:53-64
# asked: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest
from pymonet.monad_try import Try

def test_try_bind_success():
    # Arrange
    success_try = Try(value=10, is_success=True)
    binder = lambda x: Try(value=x * 2, is_success=True)
    
    # Act
    result = success_try.bind(binder)
    
    # Assert
    assert result.is_success
    assert result.value == 20

def test_try_bind_failure():
    # Arrange
    failure_try = Try(value="error", is_success=False)
    binder = lambda x: Try(value=x * 2, is_success=True)
    
    # Act
    result = failure_try.bind(binder)
    
    # Assert
    assert not result.is_success
    assert result.value == "error"
