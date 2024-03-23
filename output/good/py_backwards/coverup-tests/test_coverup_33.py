# file py_backwards/utils/snippet.py:46-48
# lines [46, 47, 48]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

@pytest.fixture
def variables_replacer():
    return VariablesReplacer(variables={})

def test_visit_attribute_replacement(variables_replacer):
    # Create a node that has an attribute with a 'name' field
    node = ast.Attribute(value=ast.Name(id='value', ctx=ast.Load()), attr='name', ctx=ast.Load())

    # Mock the _replace_field_or_node method to replace 'name' with 'new_name'
    def mock_replace_field_or_node(node, field):
        if field == 'name':
            node.attr = 'new_name'
        return node

    variables_replacer._replace_field_or_node = mock_replace_field_or_node

    # Visit the node
    new_node = variables_replacer.visit_Attribute(node)

    # Check that the 'name' attribute of the node has been replaced with 'new_name'
    assert new_node.attr == 'new_name'
    # Check that the node is still an instance of ast.Attribute
    assert isinstance(new_node, ast.Attribute)
