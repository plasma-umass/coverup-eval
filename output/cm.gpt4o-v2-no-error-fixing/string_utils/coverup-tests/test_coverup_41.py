# file: string_utils/manipulation.py:324-354
# asked: {"lines": [341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}
# gained: {"lines": [341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}

import pytest
from string_utils.manipulation import snake_case_to_camel
from string_utils.errors import InvalidInputError

def test_snake_case_to_camel_invalid_input():
    with pytest.raises(InvalidInputError):
        snake_case_to_camel(123)  # Not a string

def test_snake_case_to_camel_not_snake_case():
    assert snake_case_to_camel("notSnakeCase") == "notSnakeCase"

def test_snake_case_to_camel_valid_snake_case():
    assert snake_case_to_camel("the_snake_is_green") == "TheSnakeIsGreen"

def test_snake_case_to_camel_valid_snake_case_lower_first():
    assert snake_case_to_camel("the_snake_is_green", upper_case_first=False) == "theSnakeIsGreen"

def test_snake_case_to_camel_custom_separator():
    assert snake_case_to_camel("the-snake-is-green", separator='-') == "TheSnakeIsGreen"

def test_snake_case_to_camel_custom_separator_lower_first():
    assert snake_case_to_camel("the-snake-is-green", upper_case_first=False, separator='-') == "theSnakeIsGreen"
