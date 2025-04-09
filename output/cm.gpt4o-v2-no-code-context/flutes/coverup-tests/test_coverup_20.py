# file: flutes/iterator.py:208-227
# asked: {"lines": [208, 227], "branches": []}
# gained: {"lines": [208, 227], "branches": []}

import pytest
import operator
from flutes.iterator import scanr

def test_scanr_with_initial_value():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_scanr_without_initial_value():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']

def test_scanr_empty_iterable_with_initial_value():
    result = scanr(operator.add, [], 0)
    assert result == [0]

def test_scanr_empty_iterable_without_initial_value():
    with pytest.raises(RuntimeError):
        scanr(operator.add, [])

def test_scanr_single_element_iterable_with_initial_value():
    result = scanr(operator.add, [1], 0)
    assert result == [1, 0]

def test_scanr_single_element_iterable_without_initial_value():
    result = scanr(operator.add, [1])
    assert result == [1]
