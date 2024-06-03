# file string_utils/validation.py:577-598
# lines [577, 595, 596, 598]
# branches ['595->596', '595->598']

import pytest
from string_utils.validation import words_count, InvalidInputError
import re

# Mocking the dependencies
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def is_string(input_string):
    return isinstance(input_string, str)

@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    mocker.patch('string_utils.validation.WORDS_COUNT_RE', WORDS_COUNT_RE)
    mocker.patch('string_utils.validation.is_string', is_string)

def test_words_count_valid_input():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('! @ # % ... []') == 0
    assert words_count('123 456 789') == 3

def test_words_count_invalid_input():
    with pytest.raises(InvalidInputError):
        words_count(12345)
    with pytest.raises(InvalidInputError):
        words_count(None)
    with pytest.raises(InvalidInputError):
        words_count(['hello', 'world'])
