# file: docstring_parser/numpydoc.py:21-24
# asked: {"lines": [21, 22, 23, 24], "branches": []}
# gained: {"lines": [21, 22, 23, 24], "branches": []}

import itertools
import pytest
from docstring_parser.numpydoc import _pairwise

def test_pairwise_with_elements():
    iterable = [1, 2, 3]
    result = list(_pairwise(iterable))
    expected = [(1, 2), (2, 3), (3, None)]
    assert result == expected

def test_pairwise_empty_iterable():
    iterable = []
    result = list(_pairwise(iterable))
    expected = []
    assert result == expected

def test_pairwise_with_end():
    iterable = [1, 2, 3]
    result = list(_pairwise(iterable, end='end'))
    expected = [(1, 2), (2, 3), (3, 'end')]
    assert result == expected
