# file: f069/__init__.py:1-21
# asked: {"lines": [1, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [1, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest
from f069 import search

def test_search_case_1():
    assert search([4, 1, 2, 2, 3, 1]) == 2

def test_search_case_2():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3

def test_search_case_3():
    assert search([5, 5, 4, 4, 4]) == -1

def test_search_single_element():
    assert search([1]) == 1

def test_search_no_valid_integer():
    assert search([5, 5, 5, 5, 5]) == 5

def test_search_multiple_valid_integers():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4

def test_search_large_numbers():
    assert search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
