# file: py_backwards/transformers/python2_future.py:14-27
# asked: {"lines": [25, 26, 27], "branches": []}
# gained: {"lines": [25, 26, 27], "branches": []}

import ast
import pytest
from py_backwards.transformers.python2_future import Python2FutureTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

@pytest.fixture
def transformer():
    return Python2FutureTransformer(tree=MockTree())

def test_visit_module(monkeypatch, transformer):
    # Create a mock for imports.get_body
    def mock_get_body(future):
        return [ast.ImportFrom(module='__future__', names=[ast.alias(name='absolute_import', asname=None)], level=0)]

    # Mock the get_body function within the transformer module
    monkeypatch.setattr('py_backwards.transformers.python2_future.imports.get_body', mock_get_body)

    # Create a simple AST module node
    node = ast.Module(body=[ast.Pass()])

    # Apply the transformer
    new_node = transformer.visit_Module(node)

    # Assertions to verify the transformation
    assert transformer._tree_changed is True
    assert isinstance(new_node.body[0], ast.ImportFrom)
    assert new_node.body[0].module == '__future__'
    assert new_node.body[0].names[0].name == 'absolute_import'
    assert isinstance(new_node.body[1], ast.Pass)
