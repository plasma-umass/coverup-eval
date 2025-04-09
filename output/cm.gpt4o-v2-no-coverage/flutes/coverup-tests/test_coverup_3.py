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
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    result = reverse_map(word_to_id)
    assert result == words

    # Test with non-string keys
    d = {1: 2, 2: 0, 3: 1}
    result = reverse_map(d)
    assert result == [2, 3, 1]

    # Test with non-consecutive ids
    d = {'a': 10, 'b': 5, 'c': 7}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a']

    # Test with negative ids
    d = {'a': -1, 'b': -3, 'c': -2}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a']
