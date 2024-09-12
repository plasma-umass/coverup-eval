# file: pymonet/either.py:70-79
# asked: {"lines": [70, 77, 79], "branches": []}
# gained: {"lines": [70, 77, 79], "branches": []}

import pytest
from pymonet.either import Either
from pymonet.lazy import Lazy

def test_either_to_lazy():
    # Create an instance of Either
    either_instance = Either(42)
    
    # Convert Either to Lazy
    lazy_instance = either_instance.to_lazy()
    
    # Assert that the returned instance is of type Lazy
    assert isinstance(lazy_instance, Lazy)
    
    # Assert that the Lazy instance contains the correct value
    assert lazy_instance.constructor_fn() == 42
