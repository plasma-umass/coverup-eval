# file: lib/ansible/module_utils/common/dict_transformations.py:79-83
# asked: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}
# gained: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}

import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

def test_snake_to_camel_no_capitalize():
    assert _snake_to_camel('snake_case') == 'snakeCase'
    assert _snake_to_camel('this_is_a_test') == 'thisIsATest'
    assert _snake_to_camel('alreadyCamel') == 'alreadyCamel'
    assert _snake_to_camel('') == ''
    assert _snake_to_camel('_leading_underscore') == 'LeadingUnderscore'
    assert _snake_to_camel('trailing_underscore_') == 'trailingUnderscore_'

def test_snake_to_camel_capitalize():
    assert _snake_to_camel('snake_case', True) == 'SnakeCase'
    assert _snake_to_camel('this_is_a_test', True) == 'ThisIsATest'
    assert _snake_to_camel('alreadyCamel', True) == 'Alreadycamel'
    assert _snake_to_camel('', True) == '_'
    assert _snake_to_camel('_leading_underscore', True) == '_LeadingUnderscore'
    assert _snake_to_camel('trailing_underscore_', True) == 'TrailingUnderscore_'
