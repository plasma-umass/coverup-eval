# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {
        'old_name': 'new_name',
        'another_old_name': 'another_new_name'
    }
    return VariablesReplacer(variables)

def test_replace_module_with_replacements(variables_replacer):
    module = 'old_name.another_old_name'
    expected = 'new_name.another_new_name'
    result = variables_replacer._replace_module(module)
    assert result == expected

def test_replace_module_without_replacements(variables_replacer):
    module = 'no_change'
    expected = 'no_change'
    result = variables_replacer._replace_module(module)
    assert result == expected

def test_replace_module_partial_replacements(variables_replacer):
    module = 'old_name.no_change'
    expected = 'new_name.no_change'
    result = variables_replacer._replace_module(module)
    assert result == expected
