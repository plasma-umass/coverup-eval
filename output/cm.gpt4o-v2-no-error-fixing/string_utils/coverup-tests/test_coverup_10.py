# file: string_utils/validation.py:577-598
# asked: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}
# gained: {"lines": [577, 595, 596, 598], "branches": [[595, 596], [595, 598]]}

import pytest
from string_utils.validation import words_count
from string_utils.errors import InvalidInputError

def test_words_count_valid_string():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('! @ # % ... []') == 0

def test_words_count_invalid_input():
    with pytest.raises(InvalidInputError):
        words_count(12345)
    with pytest.raises(InvalidInputError):
        words_count(None)
    with pytest.raises(InvalidInputError):
        words_count(['this', 'is', 'a', 'list'])
