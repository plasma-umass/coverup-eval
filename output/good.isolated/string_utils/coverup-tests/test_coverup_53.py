# file string_utils/validation.py:42-78
# lines [45, 75, 76]
# branches ['44->45']

import pytest
from string_utils.validation import __ISBNChecker
from string_utils.errors import InvalidInputError

def test_isbn_checker_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        __ISBNChecker(input_string="123")  # String input but mocked to trigger line 45

def test_isbn_checker_isbn_10_value_error(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=True)
    checker = __ISBNChecker(input_string="12345X7890")  # X will cause ValueError on int conversion
    assert not checker.is_isbn_10()  # Should pass through lines 75-76 and return False
