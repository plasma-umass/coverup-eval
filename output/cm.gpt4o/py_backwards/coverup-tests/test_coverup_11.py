# file py_backwards/transformers/return_from_generator.py:64-73
# lines [64, 65, 67, 68, 70, 71, 73]
# branches ['67->68', '67->70', '70->71', '70->73']

import ast
import pytest
from py_backwards.transformers.return_from_generator import ReturnFromGeneratorTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

def test_visit_FunctionDef(mocker):
    # Create a mock for the _find_generator_returns method
    mocker.patch.object(ReturnFromGeneratorTransformer, '_find_generator_returns', return_value=[(None, ast.Return(value=ast.Constant(value=1)))])
    # Create a mock for the _replace_return method
    mocker.patch.object(ReturnFromGeneratorTransformer, '_replace_return')

    mock_tree = MockTree()
    transformer = ReturnFromGeneratorTransformer(mock_tree)
    node = ast.FunctionDef(
        name='test_func',
        args=ast.arguments(
            posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]
        ),
        body=[ast.Return(value=ast.Constant(value=1))],
        decorator_list=[]
    )

    result_node = transformer.visit_FunctionDef(node)

    # Assertions to verify the postconditions
    assert transformer._tree_changed is True
    transformer._replace_return.assert_called_once()
    assert isinstance(result_node, ast.FunctionDef)
    assert result_node.name == 'test_func'
    assert len(result_node.body) == 1
    assert isinstance(result_node.body[0], ast.Return)
    assert isinstance(result_node.body[0].value, ast.Constant)
    assert result_node.body[0].value.value == 1
