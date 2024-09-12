# file: f110/__init__.py:1-13
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

import pytest
from f110 import exchange

def test_exchange_more_even():
    lst1 = [1, 3, 5]
    lst2 = [2, 4, 6, 8]
    result = exchange(lst1, lst2)
    assert result == "YES"

def test_exchange_more_odd():
    lst1 = [1, 3, 5, 7]
    lst2 = [2, 4]
    result = exchange(lst1, lst2)
    assert result == "NO"

def test_exchange_equal_even_odd():
    lst1 = [1, 3, 5]
    lst2 = [2, 4, 6]
    result = exchange(lst1, lst2)
    assert result == "YES"

def test_exchange_no_odd():
    lst1 = [2, 4, 6]
    lst2 = [2, 4, 6]
    result = exchange(lst1, lst2)
    assert result == "YES"

def test_exchange_no_even():
    lst1 = [1, 3, 5]
    lst2 = [1, 3, 5]
    result = exchange(lst1, lst2)
    assert result == "NO"
