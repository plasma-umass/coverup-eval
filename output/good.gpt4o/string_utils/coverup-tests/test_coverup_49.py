# file string_utils/validation.py:497-513
# lines [510, 511, 513]
# branches ['510->511', '510->513']

import pytest
from string_utils.validation import is_pangram

def test_is_pangram_with_non_string_input(mocker):
    # Mocking is_full_string to return False for non-string input
    mocker.patch('string_utils.validation.is_full_string', return_value=False)
    
    # Test with non-string input
    assert not is_pangram(12345)
    assert not is_pangram(None)
    assert not is_pangram([])

def test_is_pangram_with_valid_string(mocker):
    # Mocking is_full_string to return True for valid string input
    mocker.patch('string_utils.validation.is_full_string', return_value=True)
    
    # Test with a valid pangram
    assert is_pangram('The quick brown fox jumps over the lazy dog')
    
    # Test with a non-pangram
    assert not is_pangram('hello world')
