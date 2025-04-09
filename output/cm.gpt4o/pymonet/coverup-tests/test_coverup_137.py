# file pymonet/lazy.py:68-78
# lines [78]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_ap():
    # Mock constructor function
    def mock_constructor_fn(x):
        return x + 1

    # Create a Lazy instance with the mock constructor function
    lazy_instance = Lazy(lambda x: mock_constructor_fn(x))

    # Mock applicative function
    def mock_applicative_fn(x):
        return x * 2

    # Create another Lazy instance with the mock applicative function
    applicative_instance = Lazy(lambda x: mock_applicative_fn(x))

    # Apply the applicative to the lazy instance
    result = lazy_instance.ap(applicative_instance)

    # Assert that the result is a Lazy instance
    assert isinstance(result, Lazy)

    # Assert that the result of the Lazy instance is as expected
    assert result.get(3) == 7  # (3 * 2) + 1

    # Clean up
    del lazy_instance
    del applicative_instance
    del result
