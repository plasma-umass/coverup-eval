# file string_utils/manipulation.py:300-321
# lines [321]
# branches ['318->321']

import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_camel_case_to_snake_with_non_camel_case_string():
    # Test with a string that is not in camel case to hit line 318
    assert camel_case_to_snake('not_camel_case') == 'not_camel_case'

def test_camel_case_to_snake_with_camel_case_string():
    # Test with a camel case string to hit line 321
    assert camel_case_to_snake('ThisIsACamelCaseString') == 'this_is_a_camel_case_string'

def test_camel_case_to_snake_with_invalid_input(mocker):
    # Mock the is_string function to return False and raise InvalidInputError
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(12345)  # Pass a non-string input to raise the error
