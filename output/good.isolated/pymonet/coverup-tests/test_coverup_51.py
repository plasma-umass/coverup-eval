# file pymonet/lazy.py:128-137
# lines [128, 135, 137]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

def test_lazy_to_maybe():
    # Setup a Lazy instance with a function that returns a value
    lazy_value = Lazy(lambda: 42)
    
    # Call to_maybe to transform Lazy into a Maybe
    maybe_value = lazy_value.to_maybe()
    
    # Assert that the Maybe instance contains the correct value
    assert isinstance(maybe_value, Maybe)
    assert maybe_value.get_or_else(0) == 42

# Run the test function if the module is executed directly
if __name__ == "__main__":
    pytest.main()
