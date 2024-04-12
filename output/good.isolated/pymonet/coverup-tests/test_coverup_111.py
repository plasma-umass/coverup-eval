# file pymonet/lazy.py:9-14
# lines [9, 10]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_get():
    # Create a Lazy instance with a function that returns a value
    lazy_value = Lazy(lambda: 42)

    # Use get to execute the function and get the result
    result = lazy_value.get()

    # Assert that the result is correct
    assert result == 42

    # Create a Lazy instance with a function that raises an exception
    lazy_exception = Lazy(lambda: (_ for _ in ()).throw(ValueError('error')))

    # Use get to execute the function and assert that the exception is raised
    with pytest.raises(ValueError) as exc_info:
        lazy_exception.get()

    # Assert that the exception message is correct
    assert str(exc_info.value) == 'error'
