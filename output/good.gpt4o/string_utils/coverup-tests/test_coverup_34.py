# file string_utils/manipulation.py:324-354
# lines [324, 341, 342, 344, 345, 347, 349, 350, 352, 354]
# branches ['341->342', '341->344', '344->345', '344->347', '349->350', '349->352']

import pytest
from string_utils.manipulation import snake_case_to_camel, InvalidInputError

def is_string(input_string):
    return isinstance(input_string, str)

def is_snake_case(input_string, separator):
    return all(c.islower() or c == separator for c in input_string)

def is_full_string(s):
    return bool(s)

def test_snake_case_to_camel_valid_input():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

def test_snake_case_to_camel_invalid_input():
    with pytest.raises(InvalidInputError):
        snake_case_to_camel(123)
    assert snake_case_to_camel('TheSnakeIsGreen') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green_', separator='_') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake__is_green', separator='_') == 'TheSnakeIsGreen'

@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    mocker.patch('string_utils.manipulation.is_string', side_effect=is_string)
    mocker.patch('string_utils.manipulation.is_snake_case', side_effect=is_snake_case)
    mocker.patch('string_utils.manipulation.is_full_string', side_effect=is_full_string)
