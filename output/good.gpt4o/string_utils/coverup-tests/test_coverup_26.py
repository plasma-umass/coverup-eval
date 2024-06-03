# file string_utils/manipulation.py:300-321
# lines [300, 315, 316, 318, 319, 321]
# branches ['315->316', '315->318', '318->319', '318->321']

import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError
from string_utils.validation import is_string, is_camel_case
import re

# Mocking the regex pattern used in the function
CAMEL_CASE_REPLACE_RE = re.compile(r'([a-z])([A-Z])')

@pytest.fixture
def mock_is_string(mocker):
    return mocker.patch('string_utils.manipulation.is_string')

@pytest.fixture
def mock_is_camel_case(mocker):
    return mocker.patch('string_utils.manipulation.is_camel_case')

def test_camel_case_to_snake_valid_input(mock_is_string, mock_is_camel_case):
    mock_is_string.return_value = True
    mock_is_camel_case.return_value = True
    input_string = 'ThisIsACamelStringTest'
    expected_output = 'this_is_a_camel_string_test'
    assert camel_case_to_snake(input_string) == expected_output

def test_camel_case_to_snake_invalid_input(mock_is_string):
    mock_is_string.return_value = False
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(123)

def test_camel_case_to_snake_not_camel_case(mock_is_string, mock_is_camel_case):
    mock_is_string.return_value = True
    mock_is_camel_case.return_value = False
    input_string = 'notCamelCase'
    assert camel_case_to_snake(input_string) == input_string

def test_camel_case_to_snake_custom_separator(mock_is_string, mock_is_camel_case):
    mock_is_string.return_value = True
    mock_is_camel_case.return_value = True
    input_string = 'ThisIsACamelStringTest'
    separator = '-'
    expected_output = 'this-is-a-camel-string-test'
    assert camel_case_to_snake(input_string, separator) == expected_output
