# file string_utils/validation.py:577-598
# lines [577, 595, 596, 598]
# branches ['595->596', '595->598']

import pytest
from string_utils.validation import words_count, InvalidInputError

def test_words_count_with_special_characters():
    assert words_count('! @ # % ... []') == 0

def test_words_count_with_punctuation():
    assert words_count('one,two,three.stop') == 4

def test_words_count_with_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        words_count(123)
