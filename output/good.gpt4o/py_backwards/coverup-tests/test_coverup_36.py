# file py_backwards/utils/snippet.py:76-79
# lines [76, 77, 78, 79]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_alias(mocker):
    # Mock the variables argument required by VariablesReplacer
    mock_variables = mocker.Mock()
    replacer = VariablesReplacer(mock_variables)
    
    # Mock the _replace_module and _replace_field_or_node methods
    mocker.patch.object(replacer, '_replace_module', return_value='replaced_module')
    mocker.patch.object(replacer, '_replace_field_or_node', side_effect=lambda node, field: setattr(node, field, 'replaced_asname') or node)
    
    alias_node = ast.alias(name='original_name', asname='original_asname')
    
    result_node = replacer.visit_alias(alias_node)
    
    # Assertions to verify the postconditions
    assert result_node.name == 'replaced_module'
    assert result_node.asname == 'replaced_asname'
    assert isinstance(result_node, ast.alias)
