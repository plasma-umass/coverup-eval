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
    d = {i: 99 - i for i in range(100)}
    result = reverse_map(d)
    assert result == list(range(99, -1, -1))

    # Test with non-consecutive ids
    d = {'a': 10, 'b': 5, 'c': 0}
    result = reverse_map(d)
    assert result == ['c', 'b', 'a']

