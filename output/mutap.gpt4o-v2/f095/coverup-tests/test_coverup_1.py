# file: f095/__init__.py:1-24
# asked: {"lines": [1, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [1, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [19, 20], [19, 23]]}

import pytest
from f095 import check_dict_case

def test_check_dict_case_empty_dict():
    assert check_dict_case({}) == False

def test_check_dict_case_all_uppercase():
    assert check_dict_case({'A': 1, 'B': 2}) == True

def test_check_dict_case_all_lowercase():
    assert check_dict_case({'a': 1, 'b': 2}) == True

def test_check_dict_case_mixed_case():
    assert check_dict_case({'A': 1, 'b': 2}) == False

def test_check_dict_case_non_string_keys():
    assert check_dict_case({1: 'a', 2: 'b'}) == False

def test_check_dict_case_mixed_keys():
    assert check_dict_case({'A': 1, 2: 'b'}) == False
