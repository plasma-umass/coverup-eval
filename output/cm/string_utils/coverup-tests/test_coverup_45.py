# file string_utils/manipulation.py:300-321
# lines [315, 316, 318, 319, 321]
# branches ['315->316', '315->318', '318->319', '318->321']

import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_camel_case_to_snake_with_invalid_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(123)

def test_camel_case_to_snake_with_non_camel_case_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=True)
    mocker.patch('string_utils.manipulation.is_camel_case', return_value=False)
    assert camel_case_to_snake('not_camel_case') == 'not_camel_case'
