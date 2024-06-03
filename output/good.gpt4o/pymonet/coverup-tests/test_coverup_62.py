# file pymonet/lazy.py:24-25
# lines [24, 25]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_str(mocker):
    # Mock the constructor function
    mock_constructor_fn = mocker.Mock()
    
    # Create an instance of Lazy
    lazy_instance = Lazy(mock_constructor_fn)
    
    # Manually set the attributes to ensure the __str__ method is covered
    lazy_instance.constructor_fn = "mock_constructor_fn"
    lazy_instance.value = "mock_value"
    lazy_instance.is_evaluated = True
    
    # Call the __str__ method and assert the expected output
    expected_str = 'Lazy[fn=mock_constructor_fn, value=mock_value, is_evaluated=True]'
    assert str(lazy_instance) == expected_str
