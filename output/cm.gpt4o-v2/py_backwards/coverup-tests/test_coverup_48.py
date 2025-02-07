# file: py_backwards/utils/snippet.py:38-40
# asked: {"lines": [38, 39, 40], "branches": []}
# gained: {"lines": [38, 39, 40], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def replacer():
    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self, variables):
            super().__init__(variables)

    return TestVariablesReplacer

def test_visit_name_replaces_id(replacer):
    variables = {'x': 'y'}
    replacer_instance = replacer(variables)
    node = ast.Name(id='x', ctx=ast.Load())
    new_node = replacer_instance.visit_Name(node)
    assert new_node.id == 'y'

def test_visit_name_generic_visit(replacer):
    variables = {}
    replacer_instance = replacer(variables)
    node = ast.Name(id='x', ctx=ast.Load())
    new_node = replacer_instance.visit_Name(node)
    assert new_node.id == 'x'
