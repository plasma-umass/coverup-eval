# file: pymonet/lazy.py:128-137
# asked: {"lines": [128, 135, 137], "branches": []}
# gained: {"lines": [128, 135, 137], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

class TestLazy:
    
    def test_to_maybe(self, mocker):
        # Arrange
        mock_constructor_fn = mocker.Mock(return_value=42)
        lazy_instance = Lazy(mock_constructor_fn)
        
        # Act
        maybe_instance = lazy_instance.to_maybe()
        
        # Assert
        assert isinstance(maybe_instance, Maybe)
        assert maybe_instance == Maybe.just(42)
        
        # Clean up
        mock_constructor_fn.reset_mock()
