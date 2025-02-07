# file: flutes/iterator.py:208-227
# asked: {"lines": [208, 227], "branches": []}
# gained: {"lines": [208, 227], "branches": []}

import operator
from flutes.iterator import scanr

def test_scanr_with_initial():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_scanr_without_initial():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']
