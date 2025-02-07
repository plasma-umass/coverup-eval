# file: src/blib2to3/pgen2/tokenize.py:74-75
# asked: {"lines": [74, 75], "branches": []}
# gained: {"lines": [74, 75], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import _combinations

def test_combinations():
    result = _combinations("a", "b", "c")
    expected = {"ab", "ac", "ba", "bc", "ca", "cb", "a", "b", "c"}
    assert result == expected

    result = _combinations("A", "b")
    expected = {"Ab", "bA", "A", "b"}
    assert result == expected

    result = _combinations("a", "A")
    expected = {"a", "A"}
    assert result == expected

    result = _combinations("a", "b", "B")
    expected = {"ab", "aB", "ba", "Ba", "a", "b", "B"}
    assert result == expected

    result = _combinations("a",)
    expected = {"a"}
    assert result == expected

    result = _combinations()
    expected = set()
    assert result == expected
