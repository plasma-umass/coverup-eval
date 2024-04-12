# file string_utils/validation.py:451-494
# lines [451, 471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494]
# branches ['471->472', '471->474', '474->475', '474->477', '483->484', '483->494', '487->488', '487->491', '491->483', '491->492']

import pytest
from string_utils.validation import is_palindrome

def test_is_palindrome_with_non_string_input():
    assert not is_palindrome(None), "None should not be considered a palindrome"
    assert not is_palindrome(123), "Numeric input should not be considered a palindrome"
    assert not is_palindrome([]), "List input should not be considered a palindrome"
    assert not is_palindrome({}), "Dictionary input should not be considered a palindrome"

def test_is_palindrome_with_spaces():
    assert is_palindrome("nurses run", ignore_spaces=True), "Should be considered a palindrome when ignoring spaces"
    assert not is_palindrome("nurses run"), "Should not be considered a palindrome when not ignoring spaces"

def test_is_palindrome_with_case():
    assert is_palindrome("Racecar", ignore_case=True), "Should be considered a palindrome when ignoring case"
    assert not is_palindrome("Racecar"), "Should not be considered a palindrome when not ignoring case"

def test_is_palindrome_with_spaces_and_case():
    assert is_palindrome("A man a plan a canal Panama", ignore_spaces=True, ignore_case=True), "Should be considered a palindrome when ignoring spaces and case"
    assert not is_palindrome("A man a plan a canal Panama", ignore_spaces=False, ignore_case=False), "Should not be considered a palindrome when not ignoring spaces and case"
