# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [], "branches": [[65, 68]]}
# gained: {"lines": [], "branches": [[65, 68]]}

import pytest
import ast

from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self):
            self._variables = {'os': 'operating_system', 'sys': 123}
    
    replacer = TestVariablesReplacer()
    return replacer

def test_replace_module_with_string_variable(variables_replacer):
    result = variables_replacer._replace_module('os.path')
    assert result == 'operating_system.path'

def test_replace_module_with_non_string_variable(variables_replacer):
    result = variables_replacer._replace_module('sys.path')
    assert result == 'sys.path'

def test_replace_module_with_no_variable(variables_replacer):
    result = variables_replacer._replace_module('random.module')
    assert result == 'random.module'
