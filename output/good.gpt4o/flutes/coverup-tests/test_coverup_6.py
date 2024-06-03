# file flutes/iterator.py:208-227
# lines [208, 227]
# branches []

import pytest
import operator
from flutes.iterator import scanr

def test_scanr():
    # Test with operator.add and initial value
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

    # Test with lambda function and no initial value
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']

    # Test with empty iterable and initial value
    result = scanr(operator.add, [], 0)
    assert result == [0]

    # Test with single element iterable and no initial value
    result = scanr(operator.add, [1])
    assert result == [1]

    # Test with single element iterable and initial value
    result = scanr(operator.add, [1], 0)
    assert result == [1, 0]

    # Test with different function and initial value
    result = scanr(lambda s, x: s * x, [1, 2, 3, 4], 1)
    assert result == [24, 24, 12, 4, 1]

    # Test with different function and no initial value
    result = scanr(lambda s, x: s * x, [1, 2, 3, 4])
    assert result == [24, 24, 12, 4]

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No specific cleanup needed for this test
