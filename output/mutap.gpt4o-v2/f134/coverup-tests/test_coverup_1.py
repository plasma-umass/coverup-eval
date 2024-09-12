# file: f134/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f134 import check_if_last_char_is_a_letter

def test_check_if_last_char_is_a_letter_with_letter():
    assert check_if_last_char_is_a_letter("Hello a") == True

def test_check_if_last_char_is_a_letter_with_non_letter():
    assert check_if_last_char_is_a_letter("Hello 1") == False

def test_check_if_last_char_is_a_letter_with_empty_string():
    assert check_if_last_char_is_a_letter("") == False

def test_check_if_last_char_is_a_letter_with_multiple_words():
    assert check_if_last_char_is_a_letter("Hello world z") == True

def test_check_if_last_char_is_a_letter_with_special_char():
    assert check_if_last_char_is_a_letter("Hello @") == False
