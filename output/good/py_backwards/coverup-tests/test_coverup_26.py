# file py_backwards/utils/snippet.py:72-74
# lines [72, 73, 74]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

# Test function to cover the visit_ImportFrom method
def test_visit_import_from(mocker):
    # Mock the _replace_module method to return a specific value
    mocker.patch.object(VariablesReplacer, '_replace_module', return_value='replaced_module')

    # Create an ImportFrom node to be visited
    import_from_node = ast.ImportFrom(module='original_module', names=[], level=0)

    # Instantiate the VariablesReplacer with a dummy variables dictionary and visit the ImportFrom node
    replacer = VariablesReplacer(variables={})
    new_node = replacer.visit_ImportFrom(import_from_node)

    # Assert that the module name has been replaced
    assert new_node.module == 'replaced_module'
    # Assert that the new_node is still an instance of ast.ImportFrom
    assert isinstance(new_node, ast.ImportFrom)

    # Cleanup is handled by pytest-mock through the mocker fixture
