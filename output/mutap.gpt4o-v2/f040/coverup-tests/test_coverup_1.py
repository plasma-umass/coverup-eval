# file: f040/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest
from f040 import triples_sum_to_zero

def test_triples_sum_to_zero_with_zero_sum():
    assert triples_sum_to_zero([1, -1, 0]) == True

def test_triples_sum_to_zero_without_zero_sum():
    assert triples_sum_to_zero([1, 2, 3]) == False

def test_triples_sum_to_zero_with_empty_list():
    assert triples_sum_to_zero([]) == False

def test_triples_sum_to_zero_with_no_triplets():
    assert triples_sum_to_zero([1, 2]) == False

def test_triples_sum_to_zero_with_multiple_triplets():
    assert triples_sum_to_zero([1, -1, 0, 2, -2]) == True
