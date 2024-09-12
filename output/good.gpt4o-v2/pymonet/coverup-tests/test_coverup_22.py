# file: pymonet/monad_try.py:53-64
# asked: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest
from pymonet.monad_try import Try

def test_try_bind_success():
    # Arrange
    success_try = Try(10, True)
    
    # Act
    result = success_try.bind(lambda x: Try(x + 5, True))
    
    # Assert
    assert result == Try(15, True)

def test_try_bind_failure():
    # Arrange
    failure_try = Try(10, False)
    
    # Act
    result = failure_try.bind(lambda x: Try(x + 5, True))
    
    # Assert
    assert result == failure_try
