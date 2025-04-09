# file flutils/decorators.py:57-59
# lines [57, 58, 59]
# branches []

import pytest
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_cached_property_initialization(self):
        def sample_func():
            """Sample docstring"""
            return 42

        cached_prop = cached_property(sample_func)
        
        # Assertions to verify the postconditions
        assert cached_prop.func == sample_func
        assert cached_prop.__doc__ == "Sample docstring"
