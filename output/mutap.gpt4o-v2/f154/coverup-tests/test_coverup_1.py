# file: f154/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest
from f154 import cycpattern_check

def test_cycpattern_check_true():
    assert cycpattern_check("abcde", "cde") == True

def test_cycpattern_check_false():
    assert cycpattern_check("abcde", "xyz") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abcde", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_b_in_middle():
    assert cycpattern_check("abcde", "bcd") == True

def test_cycpattern_check_b_at_start():
    assert cycpattern_check("abcde", "abc") == True

def test_cycpattern_check_b_at_end():
    assert cycpattern_check("abcde", "de") == True
