# file: flutils/decorators.py:57-59
# asked: {"lines": [57, 58, 59], "branches": []}
# gained: {"lines": [57, 58, 59], "branches": []}

import pytest
from flutils.decorators import cached_property

class TestCachedProperty:
    def test_cached_property_init(self):
        def sample_func():
            """Sample docstring"""
            return 42

        # Create an instance of cached_property
        cached_prop = cached_property(sample_func)

        # Assertions to verify the postconditions
        assert cached_prop.__doc__ == "Sample docstring"
        assert cached_prop.func == sample_func
