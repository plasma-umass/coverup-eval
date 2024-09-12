# file: f141/__init__.py:1-16
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest
from f141 import file_name_check

def test_file_name_check_valid_txt():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_valid_exe():
    assert file_name_check("example.exe") == "Yes"

def test_file_name_check_valid_dll():
    assert file_name_check("example.dll") == "Yes"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == "No"

def test_file_name_check_no_extension():
    assert file_name_check("example") == "No"

def test_file_name_check_empty_name():
    assert file_name_check(".txt") == "No"

def test_file_name_check_non_alpha_start():
    assert file_name_check("1example.txt") == "No"

def test_file_name_check_too_many_digits():
    assert file_name_check("examp1234le.txt") == "No"

def test_file_name_check_valid_with_digits():
    assert file_name_check("exam123le.txt") == "Yes"
