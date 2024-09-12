# file: f010/__init__.py:6-16
# asked: {"lines": [6, 8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [6, 8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import pytest
from f010 import make_palindrome

def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_character():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_already_palindrome():
    assert make_palindrome('aba') == 'aba'

def test_make_palindrome_non_palindrome():
    assert make_palindrome('abc') == 'abcba'

def test_make_palindrome_longer_non_palindrome():
    assert make_palindrome('abcd') == 'abcdcba'
