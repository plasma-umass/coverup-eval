# file: string_utils/validation.py:451-494
# asked: {"lines": [451, 471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494], "branches": [[471, 472], [471, 474], [474, 475], [474, 477], [483, 484], [483, 494], [487, 488], [487, 491], [491, 483], [491, 492]]}
# gained: {"lines": [451, 471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494], "branches": [[471, 472], [471, 474], [474, 475], [474, 477], [483, 484], [483, 494], [487, 488], [487, 491], [491, 483], [491, 492]]}

import pytest
from string_utils.validation import is_palindrome

def test_is_palindrome_with_non_string():
    assert not is_palindrome(12345)

def test_is_palindrome_with_empty_string():
    assert not is_palindrome("")

def test_is_palindrome_with_spaces_ignored():
    assert is_palindrome("A man a plan a canal Panama", ignore_spaces=True, ignore_case=True)

def test_is_palindrome_with_case_ignored():
    assert is_palindrome("Madam", ignore_case=True)

def test_is_palindrome_with_non_palindrome():
    assert not is_palindrome("Hello")

def test_is_palindrome_with_palindrome():
    assert is_palindrome("racecar")

def test_is_palindrome_with_spaces_and_case_ignored():
    assert is_palindrome("A Santa at NASA", ignore_spaces=True, ignore_case=True)
