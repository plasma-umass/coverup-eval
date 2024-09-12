# file: lib/ansible/module_utils/common/dict_transformations.py:79-83
# asked: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}
# gained: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}

import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

def test_snake_to_camel_with_capitalize_first():
    assert _snake_to_camel('snake_case_string', True) == 'SnakeCaseString'
    assert _snake_to_camel('another_example', True) == 'AnotherExample'
    assert _snake_to_camel('single', True) == 'Single'
    assert _snake_to_camel('_leading_underscore', True) == '_LeadingUnderscore'
    assert _snake_to_camel('trailing_underscore_', True) == 'TrailingUnderscore_'

def test_snake_to_camel_without_capitalize_first():
    assert _snake_to_camel('snake_case_string') == 'snakeCaseString'
    assert _snake_to_camel('another_example') == 'anotherExample'
    assert _snake_to_camel('single') == 'single'
    assert _snake_to_camel('_leading_underscore') == 'LeadingUnderscore'
    assert _snake_to_camel('trailing_underscore_') == 'trailingUnderscore_'
