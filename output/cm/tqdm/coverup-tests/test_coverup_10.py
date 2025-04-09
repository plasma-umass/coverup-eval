# file tqdm/auto.py:38-42
# lines [38, 42]
# branches []

import pytest
from tqdm.auto import trange

# Test function for trange to improve coverage
def test_trange():
    # Call trange with some arguments
    iterator = trange(5, desc='Testing trange', leave=False)

    # Check if the return value is an instance of tqdm
    assert hasattr(iterator, "__iter__"), "trange did not return an iterable object"

    # Check if the iterator works as expected
    assert list(iterator) == list(range(5)), "trange did not iterate over the correct range"

    # Cleanup: close the tqdm iterator to avoid side effects
    iterator.close()
