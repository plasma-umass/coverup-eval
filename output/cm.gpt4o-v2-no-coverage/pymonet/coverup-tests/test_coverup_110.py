# file: pymonet/lazy.py:151-160
# asked: {"lines": [151, 158, 160], "branches": []}
# gained: {"lines": [151, 158, 160], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

class TestLazy:
    def test_to_validation(self, mocker):
        # Arrange
        constructor_fn = mocker.Mock()
        lazy_instance = Lazy(constructor_fn)
        mock_value = "test_value"
        mock_get = mocker.patch.object(lazy_instance, 'get', return_value=mock_value)
        
        # Act
        result = lazy_instance.to_validation()
        
        # Assert
        mock_get.assert_called_once_with()
        assert isinstance(result, Validation)
        assert result.value == mock_value
        assert result.errors == []

    def test_get_evaluated(self, mocker):
        # Arrange
        constructor_fn = mocker.Mock()
        lazy_instance = Lazy(constructor_fn)
        lazy_instance.is_evaluated = True
        lazy_instance.value = "cached_value"
        
        # Act
        result = lazy_instance.get()
        
        # Assert
        assert result == "cached_value"

    def test_get_not_evaluated(self, mocker):
        # Arrange
        constructor_fn = mocker.Mock()
        lazy_instance = Lazy(constructor_fn)
        lazy_instance.is_evaluated = False
        mock_compute_value = mocker.patch.object(lazy_instance, '_compute_value', return_value="computed_value")
        
        # Act
        result = lazy_instance.get()
        
        # Assert
        mock_compute_value.assert_called_once_with()
        assert result == "computed_value"
