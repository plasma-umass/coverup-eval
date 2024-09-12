# file: f143/__init__.py:1-13
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

import pytest
from f143 import words_in_sentence

def test_words_in_sentence_single_character():
    result = words_in_sentence("a")
    assert result == ""

def test_words_in_sentence_prime_length_words():
    result = words_in_sentence("this is a test")
    assert result == "is"

def test_words_in_sentence_non_prime_length_words():
    result = words_in_sentence("hello world")
    assert result == "hello world"

def test_words_in_sentence_mixed():
    result = words_in_sentence("a ab abc abcd abcde")
    assert result == "ab abc abcde"

def test_words_in_sentence_empty_string():
    result = words_in_sentence("")
    assert result == ""

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to set up test environment
    yield
    # Code to clean up after tests
