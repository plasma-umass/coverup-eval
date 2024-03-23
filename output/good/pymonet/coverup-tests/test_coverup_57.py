# file pymonet/lazy.py:106-115
# lines [106, 113, 115]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_to_box():
    # Setup: Create a Lazy instance with a function that returns a value
    lazy_value = Lazy(lambda: 42)

    # Exercise: Transform Lazy into Box
    box = lazy_value.to_box()

    # Verify: Check if the Box contains the correct value
    # Box uses 'value' attribute instead of 'get' method
    assert box.value == 42

    # Cleanup: No cleanup required as no external state was modified
