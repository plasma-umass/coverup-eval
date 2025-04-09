# file: flutes/iterator.py:310-311
# asked: {"lines": [310, 311], "branches": []}
# gained: {"lines": [310, 311], "branches": []}

import pytest
from flutes.iterator import Range

def test_range_init_with_start_stop():
    # Test the __init__ method with start and stop parameters
    r = Range(1, 10)
    assert isinstance(r, Range)
    # Verify the length of the range
    assert len(r) == 9
    # Verify the elements in the range
    assert list(r) == list(range(1, 10))

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code to avoid state pollution
    yield
    # Add any necessary cleanup code here
