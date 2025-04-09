# file py_backwards/utils/snippet.py:62-70
# lines [62, 63, 64, 65, 66, 68, 70]
# branches ['64->65', '64->68', '65->66', '65->68']

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'old_module': 'new_module', 'old_str': 'new_str'}
    return VariablesReplacer(variables)

def test_replace_module_with_variables(variables_replacer):
    replaced_module = variables_replacer._replace_module('old_module.submodule')
    assert replaced_module == 'new_module.submodule'

def test_replace_module_without_variables(variables_replacer):
    replaced_module = variables_replacer._replace_module('unaffected.module')
    assert replaced_module == 'unaffected.module'

def test_replace_module_with_str_variable(variables_replacer):
    replaced_module = variables_replacer._replace_module('old_str.submodule')
    assert replaced_module == 'new_str.submodule'
