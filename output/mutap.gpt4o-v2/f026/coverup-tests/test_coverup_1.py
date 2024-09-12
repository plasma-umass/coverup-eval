# file: f026/__init__.py:4-8
# asked: {"lines": [4, 6, 7, 8], "branches": []}
# gained: {"lines": [4, 6, 7, 8], "branches": []}

import pytest
from f026 import remove_duplicates

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 4]) == [1, 3]

def test_remove_duplicates_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == []

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([1]) == [1]
