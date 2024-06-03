# file flutes/iterator.py:316-328
# lines [317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328]
# branches ['317->318', '317->319', '319->320', '319->324']

import pytest
from flutes.iterator import Range

def test_range_initialization():
    # Test with no arguments
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range()

    # Test with more than 3 arguments
    with pytest.raises(ValueError, match="Range should be called the same way as the builtin `range`"):
        Range(1, 2, 3, 4)

    # Test with one argument
    r = Range(5)
    assert r.l == 0
    assert r.r == 5
    assert r.step == 1
    assert r.val == 0
    assert r.length == 5

    # Test with two arguments
    r = Range(1, 5)
    assert r.l == 1
    assert r.r == 5
    assert r.step == 1
    assert r.val == 1
    assert r.length == 4

    # Test with three arguments
    r = Range(1, 5, 2)
    assert r.l == 1
    assert r.r == 5
    assert r.step == 2
    assert r.val == 1
    assert r.length == 2

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
