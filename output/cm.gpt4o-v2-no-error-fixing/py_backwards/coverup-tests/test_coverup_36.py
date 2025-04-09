# file: py_backwards/utils/snippet.py:72-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def replacer():
    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self, variables):
            self._variables = variables

    return TestVariablesReplacer

def test_visit_import_from(replacer):
    variables = {'old_module': 'new_module'}
    replacer_instance = replacer(variables)
    
    node = ast.ImportFrom(module='old_module', names=[], level=0)
    new_node = replacer_instance.visit_ImportFrom(node)
    
    assert new_node.module == 'new_module'
    assert isinstance(new_node, ast.ImportFrom)

