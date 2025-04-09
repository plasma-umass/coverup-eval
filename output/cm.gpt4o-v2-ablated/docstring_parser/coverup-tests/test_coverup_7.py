# file: docstring_parser/numpydoc.py:21-24
# asked: {"lines": [21, 22, 23, 24], "branches": []}
# gained: {"lines": [21, 22, 23, 24], "branches": []}

import itertools
import pytest
from docstring_parser.numpydoc import _pairwise

def test_pairwise_basic():
    iterable = [1, 2, 3, 4]
    result = list(_pairwise(iterable))
    expected = [(1, 2), (2, 3), (3, 4), (4, None)]
    assert result == expected

def test_pairwise_with_end():
    iterable = [1, 2, 3, 4]
    result = list(_pairwise(iterable, end='end'))
    expected = [(1, 2), (2, 3), (3, 4), (4, 'end')]
    assert result == expected

def test_pairwise_empty():
    iterable = []
    result = list(_pairwise(iterable))
    expected = []
    assert result == expected

def test_pairwise_single_element():
    iterable = [1]
    result = list(_pairwise(iterable))
    expected = [(1, None)]
    assert result == expected

def test_pairwise_two_elements():
    iterable = [1, 2]
    result = list(_pairwise(iterable))
    expected = [(1, 2), (2, None)]
    assert result == expected
