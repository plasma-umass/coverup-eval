# file: f082/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest
from f082 import prime_length

def test_prime_length_empty_string():
    assert prime_length("") == False

def test_prime_length_single_char_string():
    assert prime_length("a") == False

def test_prime_length_non_prime_length_string():
    assert prime_length("abcd") == False

def test_prime_length_prime_length_string():
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcde") == True
