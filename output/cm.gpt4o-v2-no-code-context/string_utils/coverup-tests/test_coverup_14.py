# file: string_utils/validation.py:577-598
# asked: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}
# gained: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}

import pytest
from string_utils.validation import words_count, InvalidInputError
import re

WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_words_count_valid_string():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('! @ # % ... []') == 0
    assert words_count('123 456 789') == 3
    assert words_count('one1 two2 three3') == 3

def test_words_count_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        words_count(123)

def test_words_count_empty_string():
    assert words_count('') == 0

def test_words_count_mixed_characters():
    assert words_count('hello, world! 123') == 3
    assert words_count('foo.bar,baz') == 3
    assert words_count('foo!bar?baz') == 3
