# file string_utils/validation.py:451-494
# lines [471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494]
# branches ['471->472', '471->474', '474->475', '474->477', '483->484', '483->494', '487->488', '487->491', '491->483', '491->492']

import pytest
from string_utils.validation import is_palindrome

def test_is_palindrome_non_string_input():
    assert not is_palindrome(12345)
    assert not is_palindrome(None)
    assert not is_palindrome(['a', 'b', 'a'])

def test_is_palindrome_ignore_spaces():
    assert is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True)
    assert not is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=False)

def test_is_palindrome_ignore_case():
    assert is_palindrome('Lol', ignore_case=True)
    assert not is_palindrome('Lol', ignore_case=False)

def test_is_palindrome_ignore_spaces_and_case():
    assert is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True)
    assert not is_palindrome('A man a plan a canal Panama', ignore_spaces=False, ignore_case=True)

def test_is_palindrome_regular_cases():
    assert is_palindrome('otto')
    assert not is_palindrome('ROTFL')
    assert is_palindrome('A Santa at NASA', ignore_spaces=True, ignore_case=True)
    assert not is_palindrome('A Santa at NASA', ignore_spaces=False, ignore_case=True)
