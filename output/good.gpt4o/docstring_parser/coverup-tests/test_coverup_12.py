# file docstring_parser/numpydoc.py:21-24
# lines [21, 22, 23, 24]
# branches []

import pytest
import itertools
from docstring_parser.numpydoc import _pairwise

def test_pairwise():
    # Test with a simple iterable
    iterable = [1, 2, 3, 4]
    result = list(_pairwise(iterable))
    assert result == [(1, 2), (2, 3), (3, 4), (4, None)]

    # Test with an empty iterable
    iterable = []
    result = list(_pairwise(iterable))
    assert result == []

    # Test with a single element iterable
    iterable = [1]
    result = list(_pairwise(iterable))
    assert result == [(1, None)]

    # Test with a different fillvalue
    iterable = [1, 2, 3]
    result = list(_pairwise(iterable, end='end'))
    assert result == [(1, 2), (2, 3), (3, 'end')]

    # Test with a string iterable
    iterable = 'abc'
    result = list(_pairwise(iterable))
    assert result == [('a', 'b'), ('b', 'c'), ('c', None)]

    # Test with a tuple iterable
    iterable = (1, 2, 3)
    result = list(_pairwise(iterable))
    assert result == [(1, 2), (2, 3), (3, None)]
