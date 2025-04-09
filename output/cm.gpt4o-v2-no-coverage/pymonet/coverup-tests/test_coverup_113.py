# file: pymonet/lazy.py:24-25
# asked: {"lines": [24, 25], "branches": []}
# gained: {"lines": [24, 25], "branches": []}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_str(self):
        # Mock constructor function
        def mock_constructor_fn(x):
            return x

        # Create a Lazy instance with mock values
        lazy_instance = Lazy(mock_constructor_fn)
        lazy_instance.value = "mock_value"
        lazy_instance.is_evaluated = True

        # Assert the string representation
        expected_str = 'Lazy[fn={}, value=mock_value, is_evaluated=True]'.format(repr(mock_constructor_fn))
        assert str(lazy_instance) == expected_str
