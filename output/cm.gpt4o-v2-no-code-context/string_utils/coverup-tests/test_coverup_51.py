# file: string_utils/validation.py:497-513
# asked: {"lines": [510, 511, 513], "branches": [[510, 511], [510, 513]]}
# gained: {"lines": [510, 511, 513], "branches": [[510, 511], [510, 513]]}

import pytest
from string_utils.validation import is_pangram

def test_is_pangram_with_non_string_input():
    assert not is_pangram(None)
    assert not is_pangram(12345)
    assert not is_pangram(['a', 'b', 'c'])

def test_is_pangram_with_empty_string(monkeypatch):
    def mock_is_full_string(input_string):
        return False

    monkeypatch.setattr('string_utils.validation.is_full_string', mock_is_full_string)
    assert not is_pangram('')

def test_is_pangram_with_valid_pangram(monkeypatch):
    def mock_is_full_string(input_string):
        return True

    monkeypatch.setattr('string_utils.validation.is_full_string', mock_is_full_string)
    assert is_pangram('The quick brown fox jumps over the lazy dog')

def test_is_pangram_with_invalid_pangram(monkeypatch):
    def mock_is_full_string(input_string):
        return True

    monkeypatch.setattr('string_utils.validation.is_full_string', mock_is_full_string)
    assert not is_pangram('hello world')
