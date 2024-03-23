# file string_utils/manipulation.py:324-354
# lines [341, 342, 344, 345, 347, 349, 350, 352, 354]
# branches ['341->342', '341->344', '344->345', '344->347', '349->350', '349->352']

import pytest
from string_utils.manipulation import snake_case_to_camel
from string_utils.errors import InvalidInputError

def test_snake_case_to_camel_with_invalid_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        snake_case_to_camel('invalid_input')

def test_snake_case_to_camel_with_non_snake_case_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=True)
    mocker.patch('string_utils.manipulation.is_snake_case', return_value=False)
    assert snake_case_to_camel('not_snake_case') == 'not_snake_case'

def test_snake_case_to_camel_with_empty_string(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=True)
    mocker.patch('string_utils.manipulation.is_snake_case', return_value=True)
    mocker.patch('string_utils.manipulation.is_full_string', side_effect=lambda x: False if x == '' else True)
    assert snake_case_to_camel('___', separator='_') == ''

def test_snake_case_to_camel_with_upper_case_first_false(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=True)
    mocker.patch('string_utils.manipulation.is_snake_case', return_value=True)
    mocker.patch('string_utils.manipulation.is_full_string', return_value=True)
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
