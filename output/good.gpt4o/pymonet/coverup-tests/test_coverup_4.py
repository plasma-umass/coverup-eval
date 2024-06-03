# file pymonet/lazy.py:27-36
# lines [27, 31, 32, 33, 34, 35]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_eq(mocker):
    # Mocking the constructor function
    constructor_fn = mocker.Mock(return_value=42)
    
    # Creating two Lazy instances with the same constructor function
    lazy1 = Lazy(constructor_fn)
    lazy2 = Lazy(constructor_fn)
    
    # Evaluating both Lazy instances
    lazy1.value
    lazy2.value
    
    # Asserting that both Lazy instances are equal
    assert lazy1 == lazy2
    
    # Creating a different Lazy instance with a different constructor function
    different_constructor_fn = mocker.Mock(return_value=43)
    lazy3 = Lazy(different_constructor_fn)
    
    # Evaluating the different Lazy instance
    lazy3.value
    
    # Asserting that the different Lazy instance is not equal to the first one
    assert lazy1 != lazy3
