# file: py_backwards/utils/snippet.py:72-74
# asked: {"lines": [72, 73, 74], "branches": []}
# gained: {"lines": [72, 73, 74], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer():
    variables = {'os': 'operating_system'}
    return VariablesReplacer(variables)

def test_visit_import_from(variables_replacer):
    node = ast.ImportFrom(module='os.path', names=[], level=0)
    result = variables_replacer.visit_ImportFrom(node)
    
    assert result.module == 'operating_system.path'
    assert isinstance(result, ast.ImportFrom)

def test_replace_module(variables_replacer):
    module_name = 'os.path'
    replaced_module = variables_replacer._replace_module(module_name)
    
    assert replaced_module == 'operating_system.path'
