# file pymonet/lazy.py:95-104
# lines [95, 102, 103, 104]
# branches ['102->103', '102->104']

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_lazy_get_not_evaluated(self, mocker):
        # Mock the _compute_value method to control its behavior
        mock_compute_value = mocker.patch.object(Lazy, '_compute_value', return_value=42)
        
        # Create a dummy constructor function
        def dummy_constructor():
            return 42
        
        # Create an instance of Lazy
        lazy_instance = Lazy(dummy_constructor)
        lazy_instance.is_evaluated = False
        
        # Call the get method and assert the result
        result = lazy_instance.get()
        assert result == 42
        
        # Ensure _compute_value was called
        mock_compute_value.assert_called_once()

    def test_lazy_get_evaluated(self):
        # Create a dummy constructor function
        def dummy_constructor():
            return 42
        
        # Create an instance of Lazy
        lazy_instance = Lazy(dummy_constructor)
        lazy_instance.is_evaluated = True
        lazy_instance.value = 42
        
        # Call the get method and assert the result
        result = lazy_instance.get()
        assert result == 42
