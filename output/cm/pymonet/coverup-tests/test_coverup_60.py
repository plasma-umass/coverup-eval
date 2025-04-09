# file pymonet/lazy.py:24-25
# lines [24, 25]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_str_representation(mocker):
    # Mock the constructor function and value to avoid side effects
    mock_constructor_fn = mocker.Mock()
    mock_value = mocker.Mock()

    # Create a Lazy instance with mocked constructor and value
    lazy_instance = Lazy(mock_constructor_fn)
    lazy_instance.value = mock_value
    lazy_instance.is_evaluated = False

    # Check the __str__ representation
    expected_str = 'Lazy[fn={}, value={}, is_evaluated={}]'.format(mock_constructor_fn, mock_value, False)
    assert str(lazy_instance) == expected_str

    # Clean up by deleting the instance
    del lazy_instance
