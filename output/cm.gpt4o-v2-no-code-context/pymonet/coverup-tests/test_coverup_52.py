# file: pymonet/lazy.py:27-36
# asked: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}
# gained: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_lazy_equality(self):
        # Create a Lazy instance with a simple constructor function
        lazy1 = Lazy(lambda: 42)
        lazy2 = Lazy(lambda: 42)
        
        # Ensure they are not evaluated yet
        assert not lazy1.is_evaluated
        assert not lazy2.is_evaluated
        
        # They should not be equal because they are different instances
        assert lazy1 != lazy2
        
        # Evaluate both Lazy instances
        lazy1_value = lazy1.value
        lazy2_value = lazy2.value
        
        # They should still not be equal because they are different instances
        assert lazy1 != lazy2
        
        # Create another Lazy instance with a different constructor function
        lazy3 = Lazy(lambda: 43)
        
        # They should not be equal because they have different constructor functions
        assert lazy1 != lazy3
        
        # Evaluate the third Lazy instance
        lazy3_value = lazy3.value
        
        # They should still not be equal because they have different values
        assert lazy1 != lazy3

    def test_lazy_equality_with_non_lazy(self):
        lazy1 = Lazy(lambda: 42)
        
        # Ensure it is not evaluated yet
        assert not lazy1.is_evaluated
        
        # Compare with a non-Lazy object
        assert lazy1 != 42
        
        # Evaluate the Lazy instance
        lazy1_value = lazy1.value
        
        # Compare with a non-Lazy object again
        assert lazy1 != 42
