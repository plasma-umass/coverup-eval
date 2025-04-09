# file: src/blib2to3/pgen2/tokenize.py:74-75
# asked: {"lines": [74, 75], "branches": []}
# gained: {"lines": [74, 75], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import _combinations

def test_combinations():
    result = _combinations("a", "b", "c")
    expected = {'ab', 'ac', 'ba', 'bc', 'ca', 'cb', 'a', 'b', 'c'}
    assert result == expected

    result = _combinations("A", "b", "C")
    expected = {'Ab', 'AC', 'bA', 'bC', 'CA', 'Cb', 'A', 'b', 'C'}
    assert result == expected

    result = _combinations("a", "A")
    expected = {'a', 'A'}
    assert result == expected

    result = _combinations("a", "b", "B")
    expected = {'ab', 'aB', 'ba', 'Ba', 'a', 'b', 'B'}
    assert result == expected
