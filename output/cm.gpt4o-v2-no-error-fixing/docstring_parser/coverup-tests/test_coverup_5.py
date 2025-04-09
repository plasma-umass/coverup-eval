# file: docstring_parser/numpydoc.py:21-24
# asked: {"lines": [21, 22, 23, 24], "branches": []}
# gained: {"lines": [21, 22, 23, 24], "branches": []}

import itertools
import pytest

from docstring_parser.numpydoc import _pairwise

def test_pairwise_with_elements():
    iterable = [1, 2, 3]
    result = list(_pairwise(iterable))
    assert result == [(1, 2), (2, 3), (3, None)]

def test_pairwise_empty_iterable():
    iterable = []
    result = list(_pairwise(iterable))
    assert result == []

def test_pairwise_with_end():
    iterable = [1, 2, 3]
    result = list(_pairwise(iterable, end='end'))
    assert result == [(1, 2), (2, 3), (3, 'end')]
