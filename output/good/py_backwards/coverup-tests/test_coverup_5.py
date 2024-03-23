# file py_backwards/transformers/python2_future.py:14-27
# lines [14, 15, 22, 24, 25, 26, 27]
# branches []

import ast
from py_backwards.transformers.python2_future import Python2FutureTransformer
import pytest

def test_python2_future_transformer(mocker):
    # Mock the imports.get_body function to return an empty list
    mocker.patch('py_backwards.transformers.python2_future.imports.get_body', return_value=[])

    # Create a simple module node
    module_node = ast.Module(body=[])

    # Instantiate the transformer with a dummy tree and visit the module node
    transformer = Python2FutureTransformer(tree=ast.parse(''))
    transformed_node = transformer.visit_Module(module_node)

    # Assert that the transformer indicates the tree has changed
    assert transformer._tree_changed

    # Assert that the transformed node is still a module node
    assert isinstance(transformed_node, ast.Module)

    # Assert that the body of the transformed node is an empty list
    # (since we mocked imports.get_body to return an empty list)
    assert transformed_node.body == []

    # Cleanup: Unpatch the mocked function
    mocker.stopall()
