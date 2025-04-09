# file: flutes/structure.py:16-32
# asked: {"lines": [16, 32], "branches": []}
# gained: {"lines": [16, 32], "branches": []}

import pytest
from flutes.structure import reverse_map

def test_reverse_map():
    # Test with a simple dictionary
    d = {'a': 2, 'b': 0, 'c': 1}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a']

    # Test with an empty dictionary
    d = {}
    result = reverse_map(d)
    assert result == []

    # Test with a larger dictionary
    d = {chr(97 + i): i for i in range(100)}
    result = reverse_map(d)
    assert result == [chr(97 + i) for i in range(100)]

    # Test with non-string keys
    d = {i: i for i in range(10)}
    result = reverse_map(d)
    assert result == list(range(10))

    # Test with non-consecutive ids
    d = {'a': 0, 'b': 2, 'c': 1}
    result = reverse_map(d)
    assert result == ['a', 'c', 'b']

    # Test with negative ids
    d = {'a': -1, 'b': -3, 'c': -2}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a']

    # Test with mixed type keys
    d = {1: 2, 'a': 0, (1, 2): 1}
    result = reverse_map(d)
    assert result == ['a', (1, 2), 1]

