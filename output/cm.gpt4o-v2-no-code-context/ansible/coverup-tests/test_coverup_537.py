# file: lib/ansible/module_utils/common/dict_transformations.py:79-83
# asked: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}
# gained: {"lines": [79, 80, 81, 83], "branches": [[80, 81], [80, 83]]}

import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

def test_snake_to_camel_with_capitalize_first():
    result = _snake_to_camel('snake_case_example', capitalize_first=True)
    assert result == 'SnakeCaseExample'

def test_snake_to_camel_without_capitalize_first():
    result = _snake_to_camel('snake_case_example', capitalize_first=False)
    assert result == 'snakeCaseExample'

def test_snake_to_camel_single_word_with_capitalize_first():
    result = _snake_to_camel('example', capitalize_first=True)
    assert result == 'Example'

def test_snake_to_camel_single_word_without_capitalize_first():
    result = _snake_to_camel('example', capitalize_first=False)
    assert result == 'example'
