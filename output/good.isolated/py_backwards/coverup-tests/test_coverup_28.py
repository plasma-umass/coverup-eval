# file py_backwards/utils/snippet.py:42-44
# lines [42, 43, 44]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

# Test function to cover the visit_FunctionDef method
def test_visit_function_def(mocker):
    source_code = """
def my_function(x):
    return x + 1
"""

    # Parse the source code into an AST
    parsed_code = ast.parse(source_code)

    # Mock the variables argument required by VariablesReplacer
    variables = mocker.MagicMock()

    # Create a VariablesReplacer instance with mocked variables
    replacer = VariablesReplacer(variables)

    # Visit the FunctionDef node
    function_def_node = parsed_code.body[0]
    new_function_def_node = replacer.visit_FunctionDef(function_def_node)

    # Check that the node is still a FunctionDef node
    assert isinstance(new_function_def_node, ast.FunctionDef)

    # Check that the name of the function is unchanged
    assert new_function_def_node.name == 'my_function'

    # Check that the body of the function is unchanged
    assert ast.dump(new_function_def_node.body[0]) == ast.dump(function_def_node.body[0])

# Run the test with pytest
if __name__ == "__main__":
    pytest.main([__file__])
