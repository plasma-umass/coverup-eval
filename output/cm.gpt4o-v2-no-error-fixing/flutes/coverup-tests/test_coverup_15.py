# file: flutes/iterator.py:200-201
# asked: {"lines": [200, 201], "branches": []}
# gained: {"lines": [200, 201], "branches": []}

import pytest
from flutes.iterator import scanr

def test_scanr_no_initial():
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]

def test_scanr_with_initial():
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4], 5)
    assert result == [15, 14, 12, 9, 5]
