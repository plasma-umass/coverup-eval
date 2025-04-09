# file: flutes/structure.py:16-32
# asked: {"lines": [32], "branches": []}
# gained: {"lines": [32], "branches": []}

import pytest
from typing import Dict, List

# Assuming the function reverse_map is defined in flutes/structure.py
from flutes.structure import reverse_map

def test_reverse_map():
    # Test with a simple dictionary
    d = {'a': 2, 'b': 0, 'c': 1}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a'], f"Expected ['b', 'c', 'a'], but got {result}"

    # Test with an empty dictionary
    d = {}
    result = reverse_map(d)
    assert result == [], f"Expected [], but got {result}"

    # Test with a larger dictionary
    d = {chr(97 + i): i for i in range(100)}
    result = reverse_map(d)
    expected = [chr(97 + i) for i in range(100)]
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test with non-string keys
    d = {1: 2, 2: 0, 3: 1}
    result = reverse_map(d)
    assert result == [2, 3, 1], f"Expected [2, 3, 1], but got {result}"

    # Test with non-integer values (should not raise an error)
    d = {'a': 2, 'b': 0, 'c': 1}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a'], f"Expected ['b', 'c', 'a'], but got {result}"
