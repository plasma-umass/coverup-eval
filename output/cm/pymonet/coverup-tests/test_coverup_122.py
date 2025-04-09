# file pymonet/maybe.py:19-22
# lines [20, 21, 22]
# branches []

import pytest
from pymonet.maybe import Maybe

class Just(Maybe):
    def __init__(self, value):
        self.value = value
        self.is_nothing = False

class Nothing(Maybe):
    def __init__(self):
        self.is_nothing = True

def test_maybe_eq():
    # Test equality between Just instances with the same value
    assert Just(5) == Just(5)
    
    # Test equality between Just instances with different values
    assert Just(5) != Just(10)
    
    # Test equality between Nothing instances
    assert Nothing() == Nothing()
    
    # Test inequality between Just and Nothing instances
    assert Just(5) != Nothing()
    
    # Test inequality between Maybe and non-Maybe instances
    assert Just(5) != 5
    assert Nothing() != None
