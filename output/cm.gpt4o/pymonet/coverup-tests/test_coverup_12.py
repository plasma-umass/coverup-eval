# file pymonet/monad_try.py:92-105
# lines [92, 103, 104, 105]
# branches ['103->104', '103->105']

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_filter_success_true(self):
        # Arrange
        monad = Try(10, True)
        
        # Act
        result = monad.filter(lambda x: x > 5)
        
        # Assert
        assert result.is_success
        assert result.value == 10

    def test_filter_success_false(self):
        # Arrange
        monad = Try(10, True)
        
        # Act
        result = monad.filter(lambda x: x < 5)
        
        # Assert
        assert not result.is_success
        assert result.value == 10

    def test_filter_failure(self):
        # Arrange
        monad = Try(10, False)
        
        # Act
        result = monad.filter(lambda x: x > 5)
        
        # Assert
        assert not result.is_success
        assert result.value == 10
