# file pymonet/lazy.py:50-54
# lines [50, 51, 52, 54]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_compute_value():
    # Setup: Create a Lazy instance with a constructor function
    constructor_fn = lambda x: x * 2
    lazy_instance = Lazy(constructor_fn)

    # Precondition: Check that the value is not yet evaluated
    assert not lazy_instance.is_evaluated

    # Action: Trigger the computation of the value
    computed_value = lazy_instance._compute_value(10)

    # Postconditions: Verify the value is computed and stored correctly
    assert lazy_instance.is_evaluated
    assert computed_value == 20
    assert lazy_instance.value == 20

    # Cleanup: No cleanup required as no external resources are affected
