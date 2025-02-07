# file: string_utils/manipulation.py:324-354
# asked: {"lines": [324, 341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}
# gained: {"lines": [324, 341, 342, 344, 345, 347, 349, 350, 352, 354], "branches": [[341, 342], [341, 344], [344, 345], [344, 347], [349, 350], [349, 352]]}

import pytest
from string_utils.manipulation import snake_case_to_camel
from string_utils.errors import InvalidInputError

def test_snake_case_to_camel_valid_input():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

def test_snake_case_to_camel_invalid_string():
    with pytest.raises(InvalidInputError):
        snake_case_to_camel(123)

def test_snake_case_to_camel_not_snake_case():
    assert snake_case_to_camel('notSnakeCase') == 'notSnakeCase'
    assert snake_case_to_camel('not-snake-case', separator='_') == 'not-snake-case'

def test_snake_case_to_camel_empty_tokens():
    assert snake_case_to_camel('a__b__c') == 'ABC'
    assert snake_case_to_camel('a__b__c', upper_case_first=False) == 'aBC'
    assert snake_case_to_camel('a--b--c', separator='-') == 'ABC'
    assert snake_case_to_camel('a--b--c', upper_case_first=False, separator='-') == 'aBC'
