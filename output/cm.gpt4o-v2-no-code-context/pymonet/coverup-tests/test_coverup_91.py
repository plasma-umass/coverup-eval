# file: pymonet/lazy.py:80-93
# asked: {"lines": [80, 89, 90, 91, 93], "branches": []}
# gained: {"lines": [80, 89, 90, 91, 93], "branches": []}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_bind_executes_all_lines(self):
        # Mock function to be used with bind
        def mock_fn(value):
            return Lazy(lambda: value + 1)

        # Create a Lazy instance with a simple constructor function
        lazy_instance = Lazy(lambda: 5)

        # Bind the mock function to the lazy instance
        bound_instance = lazy_instance.bind(mock_fn)

        # Assert that the bound instance is a Lazy instance
        assert isinstance(bound_instance, Lazy)

        # Assert that the constructor function of the bound instance returns the expected value
        assert bound_instance._compute_value()() == 6

    def test_bind_with_different_function(self):
        # Mock function to be used with bind
        def mock_fn(value):
            return Lazy(lambda: value * 2)

        # Create a Lazy instance with a simple constructor function
        lazy_instance = Lazy(lambda: 3)

        # Bind the mock function to the lazy instance
        bound_instance = lazy_instance.bind(mock_fn)

        # Assert that the bound instance is a Lazy instance
        assert isinstance(bound_instance, Lazy)

        # Assert that the constructor function of the bound instance returns the expected value
        assert bound_instance._compute_value()() == 6

    def test_bind_with_complex_function(self):
        # Mock function to be used with bind
        def mock_fn(value):
            return Lazy(lambda: value ** 2)

        # Create a Lazy instance with a simple constructor function
        lazy_instance = Lazy(lambda: 4)

        # Bind the mock function to the lazy instance
        bound_instance = lazy_instance.bind(mock_fn)

        # Assert that the bound instance is a Lazy instance
        assert isinstance(bound_instance, Lazy)

        # Assert that the constructor function of the bound instance returns the expected value
        assert bound_instance._compute_value()() == 16
