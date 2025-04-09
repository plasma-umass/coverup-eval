# file string_utils/validation.py:116-138
# lines [136]
# branches ['135->136']

import pytest
from string_utils.validation import is_number

def test_is_number_with_non_string_input(mocker):
    mocker.patch('string_utils.validation.InvalidInputError', Exception)
    with pytest.raises(Exception):
        is_number(123)  # Non-string input to trigger the InvalidInputError

def test_is_number_with_string_input():
    assert is_number('42') == True
    assert is_number('19.99') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True
    assert is_number('1 2 3') == False
