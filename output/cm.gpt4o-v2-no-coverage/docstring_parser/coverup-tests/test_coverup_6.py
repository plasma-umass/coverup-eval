# file: docstring_parser/numpydoc.py:21-24
# asked: {"lines": [21, 22, 23, 24], "branches": []}
# gained: {"lines": [21, 22, 23, 24], "branches": []}

import itertools
import typing as T
import pytest

from docstring_parser.numpydoc import _pairwise

def test_pairwise_basic():
    result = list(_pairwise([1, 2, 3]))
    assert result == [(1, 2), (2, 3), (3, None)]

def test_pairwise_with_end():
    result = list(_pairwise([1, 2, 3], end=0))
    assert result == [(1, 2), (2, 3), (3, 0)]

def test_pairwise_empty():
    result = list(_pairwise([]))
    assert result == []

def test_pairwise_single_element():
    result = list(_pairwise([1]))
    assert result == [(1, None)]

def test_pairwise_single_element_with_end():
    result = list(_pairwise([1], end=0))
    assert result == [(1, 0)]
