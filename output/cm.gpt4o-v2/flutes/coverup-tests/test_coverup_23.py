# file: flutes/iterator.py:92-111
# asked: {"lines": [92, 105, 106, 107, 108, 109, 110, 111], "branches": [[106, 107], [106, 111], [107, 108], [107, 109]]}
# gained: {"lines": [92, 105, 106, 107, 108, 109, 110, 111], "branches": [[106, 107], [106, 111], [107, 108], [107, 109]]}

import pytest
from flutes.iterator import drop_until

def test_drop_until():
    # Test case where predicate is satisfied in the middle of the iterable
    result = list(drop_until(lambda x: x > 5, range(10)))
    assert result == [6, 7, 8, 9]

    # Test case where predicate is never satisfied
    result = list(drop_until(lambda x: x > 10, range(10)))
    assert result == []

    # Test case where predicate is satisfied at the first element
    result = list(drop_until(lambda x: x >= 0, range(10)))
    assert result == list(range(10))

    # Test case where predicate is satisfied at the last element
    result = list(drop_until(lambda x: x == 9, range(10)))
    assert result == [9]

    # Test case with an empty iterable
    result = list(drop_until(lambda x: x > 5, []))
    assert result == []

    # Test case with a non-integer iterable
    result = list(drop_until(lambda x: x == 'c', 'abcde'))
    assert result == ['c', 'd', 'e']
