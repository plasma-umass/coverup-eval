# file: py_backwards/utils/snippet.py:76-79
# asked: {"lines": [76, 77, 78, 79], "branches": []}
# gained: {"lines": [76, 77, 78, 79], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def replacer():
    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self):
            self._variables = {'old_name': 'new_name', 'old_asname': 'new_asname'}
    
    return TestVariablesReplacer()

def test_visit_alias(replacer):
    alias_node = ast.alias(name='old_name', asname='old_asname')
    result_node = replacer.visit_alias(alias_node)
    
    assert result_node.name == 'new_name'
    assert result_node.asname == 'new_asname'

def test_visit_alias_no_asname(replacer):
    alias_node = ast.alias(name='old_name', asname=None)
    result_node = replacer.visit_alias(alias_node)
    
    assert result_node.name == 'new_name'
    assert result_node.asname is None
