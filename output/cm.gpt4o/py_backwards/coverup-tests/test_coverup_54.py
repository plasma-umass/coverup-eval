# file py_backwards/transformers/python2_future.py:14-27
# lines [25, 26, 27]
# branches []

import ast
import pytest
from py_backwards.transformers.python2_future import Python2FutureTransformer
from py_backwards.transformers.base import BaseNodeTransformer

@pytest.fixture
def mock_imports_get_body(mocker):
    mock = mocker.patch('py_backwards.transformers.python2_future.imports.get_body')
    mock.return_value = [ast.ImportFrom(module='__future__', names=[ast.alias(name='absolute_import', asname=None)], level=0)]
    return mock

class MockTree:
    pass

def test_visit_module_executes_lines_25_27(mock_imports_get_body):
    mock_tree = MockTree()
    transformer = Python2FutureTransformer(mock_tree)
    node = ast.Module(body=[])
    
    transformed_node = transformer.visit_Module(node)
    
    # Assertions to verify the postconditions
    assert transformer._tree_changed is True
    assert isinstance(transformed_node, ast.Module)
    assert len(transformed_node.body) > 0
    assert isinstance(transformed_node.body[0], ast.ImportFrom)
    assert transformed_node.body[0].module == '__future__'
    assert transformed_node.body[0].names[0].name == 'absolute_import'
