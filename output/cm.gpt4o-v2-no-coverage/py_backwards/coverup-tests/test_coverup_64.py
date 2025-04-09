# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [], "branches": [[65, 68]]}
# gained: {"lines": [], "branches": [[65, 68]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {
        'old_name': 'new_name',
        'another_old_name': 'another_new_name',
        'unchanged_name': 123  # This should not be replaced since it's not a string
    }
    return VariablesReplacer(variables)

def test_replace_module(variables_replacer):
    # Test case where all parts are replaced
    module = 'old_name.another_old_name'
    expected = 'new_name.another_new_name'
    result = variables_replacer._replace_module(module)
    assert result == expected

    # Test case where some parts are replaced
    module = 'old_name.unchanged_name'
    expected = 'new_name.unchanged_name'
    result = variables_replacer._replace_module(module)
    assert result == expected

    # Test case where no parts are replaced
    module = 'unchanged_name'
    expected = 'unchanged_name'
    result = variables_replacer._replace_module(module)
    assert result == expected

    # Test case with empty module
    module = ''
    expected = ''
    result = variables_replacer._replace_module(module)
    assert result == expected
