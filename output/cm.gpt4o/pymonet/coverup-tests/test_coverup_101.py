# file pymonet/maybe.py:8-13
# lines [8, 9]
# branches []

import pytest
from pymonet.maybe import Maybe

def test_maybe_class():
    # Since Maybe is effectively abstract, we need to test its concrete subtypes.
    # Assuming Box and Nothing are the concrete subtypes of Maybe.
    
    class Box(Maybe):
        def __init__(self, value):
            super().__init__(value, False)
            self.value = value

    class Nothing(Maybe):
        def __init__(self):
            super().__init__(None, True)

    # Test instantiation of Box
    box_instance = Box(10)
    assert isinstance(box_instance, Maybe)
    assert box_instance.value == 10
    assert not box_instance.is_nothing

    # Test instantiation of Nothing
    nothing_instance = Nothing()
    assert isinstance(nothing_instance, Maybe)
    assert nothing_instance.is_nothing

    # Clean up
    del box_instance
    del nothing_instance
