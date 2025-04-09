# file: pymonet/lazy.py:95-104
# asked: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}
# gained: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_get_memoized_value(self, mocker):
        # Mock the _compute_value method to ensure it is not called
        lazy_instance = Lazy(lambda x: x + 1)
        lazy_instance.is_evaluated = True
        lazy_instance.value = 42

        mock_compute_value = mocker.patch.object(lazy_instance, '_compute_value')

        result = lazy_instance.get(1)
        
        assert result == 42
        mock_compute_value.assert_not_called()

    def test_get_compute_value(self, mocker):
        # Mock the _compute_value method to ensure it is called
        lazy_instance = Lazy(lambda x: x + 1)
        lazy_instance.is_evaluated = False

        mock_compute_value = mocker.patch.object(lazy_instance, '_compute_value', return_value=42)

        result = lazy_instance.get(1)
        
        assert result == 42
        mock_compute_value.assert_called_once_with(1)
