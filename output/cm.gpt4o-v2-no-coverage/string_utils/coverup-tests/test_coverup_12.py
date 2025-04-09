# file: string_utils/validation.py:577-598
# asked: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}
# gained: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}

import pytest
from string_utils.validation import words_count
from string_utils.errors import InvalidInputError
import re

# Mocking the dependencies
WORDS_COUNT_RE = re.compile(r'\b\w+\b')
def is_string(input_string):
    return isinstance(input_string, str)

def test_words_count_valid_string():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('! @ # % ... []') == 0
    assert words_count('123 456 789') == 3
    assert words_count('hello123 world456') == 2

def test_words_count_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        words_count(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    with pytest.raises(InvalidInputError) as excinfo:
        words_count(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'
