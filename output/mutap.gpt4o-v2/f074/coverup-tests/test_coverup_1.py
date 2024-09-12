# file: f074/__init__.py:1-14
# asked: {"lines": [1, 3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [1, 3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match

def test_total_match_equal_length():
    lst1 = ["a", "b"]
    lst2 = ["c", "d"]
    assert total_match(lst1, lst2) == lst1

def test_total_match_lst1_shorter():
    lst1 = ["a"]
    lst2 = ["b", "c"]
    assert total_match(lst1, lst2) == lst1

def test_total_match_lst2_shorter():
    lst1 = ["a", "b", "c"]
    lst2 = ["d"]
    assert total_match(lst1, lst2) == lst2
