# file: pymonet/lazy.py:151-160
# asked: {"lines": [158, 160], "branches": []}
# gained: {"lines": [158, 160], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

class TestLazy:
    
    def test_to_validation(self, mocker):
        # Arrange
        lazy_instance = Lazy(lambda x: x + 1)
        mocker.patch.object(lazy_instance, 'get', return_value=42)
        
        # Act
        result = lazy_instance.to_validation()
        
        # Assert
        assert isinstance(result, Validation)
        assert result.is_success()
        assert result.value == 42
