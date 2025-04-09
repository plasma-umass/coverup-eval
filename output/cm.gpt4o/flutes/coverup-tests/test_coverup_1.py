# file flutes/iterator.py:204-205
# lines [204, 205]
# branches []

import pytest
from flutes.iterator import scanr

def test_scanr_with_initial():
    def add(x, y):
        return x + y

    iterable = [1, 2, 3, 4]
    initial = 0
    result = scanr(add, iterable, initial)
    
    assert result == [10, 9, 7, 4, 0]

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
