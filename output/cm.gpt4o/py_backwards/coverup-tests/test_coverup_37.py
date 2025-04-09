# file py_backwards/utils/snippet.py:72-74
# lines [72, 73, 74]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_importfrom(mocker):
    # Mock the variables argument required by VariablesReplacer
    mock_variables = mocker.MagicMock()
    
    replacer = VariablesReplacer(mock_variables)
    
    # Mock the _replace_module method to return a specific value
    mocker.patch.object(replacer, '_replace_module', return_value='replaced_module')
    
    # Create a sample ImportFrom node
    node = ast.ImportFrom(module='original_module', names=[], level=0)
    
    # Visit the node
    result = replacer.visit_ImportFrom(node)
    
    # Assertions to verify the postconditions
    assert result.module == 'replaced_module'
    assert isinstance(result, ast.ImportFrom)
