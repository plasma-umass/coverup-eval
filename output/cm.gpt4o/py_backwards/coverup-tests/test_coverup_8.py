# file py_backwards/utils/tree.py:26-35
# lines [26, 29, 31, 32, 33, 35]
# branches ['31->32', '31->35']

import ast
import pytest
from py_backwards.utils.tree import get_non_exp_parent_and_index, get_parent

def test_get_non_exp_parent_and_index(mocker):
    # Create a sample AST tree
    source_code = """
def foo():
    if True:
        pass
"""
    tree = ast.parse(source_code)
    
    # Find the 'pass' node
    pass_node = tree.body[0].body[0].body[0]
    
    # Mock the get_parent function to return the correct parent nodes
    def mock_get_parent(tree, node):
        if isinstance(node, ast.Pass):
            return tree.body[0].body[0]
        elif isinstance(node, ast.If):
            return tree.body[0]
        return None
    
    mocker.patch('py_backwards.utils.tree.get_parent', side_effect=mock_get_parent)
    
    # Call the function to test
    parent, index = get_non_exp_parent_and_index(tree, pass_node)
    
    # Assertions to verify the postconditions
    assert isinstance(parent, ast.If)
    assert index == 0
