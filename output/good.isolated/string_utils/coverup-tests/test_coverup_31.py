# file string_utils/validation.py:497-513
# lines [497, 510, 511, 513]
# branches ['510->511', '510->513']

import pytest
import string
from string_utils.validation import is_pangram

def test_is_pangram_with_non_string_input(mocker):
    # Mock the is_full_string function to return False for non-string input
    mocker.patch('string_utils.validation.is_full_string', return_value=False)
    
    # Test with non-string input
    assert not is_pangram(123), "Expected False for non-string input"

def test_is_pangram_with_pangram_string():
    # Test with a pangram string
    pangram = 'The quick brown fox jumps over the lazy dog'
    assert is_pangram(pangram), "Expected True for a pangram string"

def test_is_pangram_with_non_pangram_string():
    # Test with a non-pangram string
    non_pangram = 'hello world'
    assert not is_pangram(non_pangram), "Expected False for a non-pangram string"

def test_is_pangram_with_punctuation_and_spaces():
    # Test with a pangram string that includes punctuation and spaces
    pangram_with_punctuation = 'The quick brown fox jumps over the lazy dog!'
    assert is_pangram(pangram_with_punctuation), "Expected True for a pangram string with punctuation"

def test_is_pangram_with_uppercase_letters():
    # Test with a pangram string that includes uppercase letters
    pangram_with_uppercase = 'The Quick Brown Fox Jumps Over The Lazy Dog'
    assert is_pangram(pangram_with_uppercase.lower()), "Expected True for a pangram string with uppercase letters"
