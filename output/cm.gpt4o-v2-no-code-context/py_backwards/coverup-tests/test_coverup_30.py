# file: py_backwards/utils/snippet.py:76-79
# asked: {"lines": [76, 77, 78, 79], "branches": []}
# gained: {"lines": [76, 77, 78, 79], "branches": []}

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

@pytest.fixture
def variables_replacer(mocker):
    mocker.patch.object(VariablesReplacer, '__init__', lambda self, variables: None)
    replacer = VariablesReplacer(variables={})
    mocker.patch.object(replacer, '_replace_module', side_effect=lambda name: name)
    mocker.patch.object(replacer, '_replace_field_or_node', side_effect=lambda node, field: node)
    return replacer

def test_visit_alias_replaces_module_name(variables_replacer, mocker):
    mocker.patch.object(variables_replacer, '_replace_module', return_value='replaced_module')
    mocker.patch.object(variables_replacer, '_replace_field_or_node', side_effect=lambda node, field: node)
    
    alias_node = ast.alias(name='original_module', asname=None)
    result_node = variables_replacer.visit_alias(alias_node)
    
    assert result_node.name == 'replaced_module'
    assert result_node.asname is None

def test_visit_alias_replaces_asname(variables_replacer, mocker):
    mocker.patch.object(variables_replacer, '_replace_module', return_value='original_module')
    mocker.patch.object(variables_replacer, '_replace_field_or_node', side_effect=lambda node, field: setattr(node, field, 'replaced_asname') or node)
    
    alias_node = ast.alias(name='original_module', asname='original_asname')
    result_node = variables_replacer.visit_alias(alias_node)
    
    assert result_node.name == 'original_module'
    assert result_node.asname == 'replaced_asname'
