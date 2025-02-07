# file: py_backwards/transformers/yield_from.py:55-65
# asked: {"lines": [55, 56, 57, 58, 59, 61, 62, 63, 64, 65], "branches": [[56, 57], [58, 59], [58, 61]]}
# gained: {"lines": [55, 56, 57, 58, 59, 61, 62, 63, 64, 65], "branches": [[56, 57], [58, 59], [58, 61]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.utils.tree import insert_at

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return YieldFromTransformer(tree)

def test_handle_assignments(transformer, mocker):
    # Mocking the methods _get_yield_from_index and _emulate_yield_from
    mocker.patch.object(transformer, '_get_yield_from_index', side_effect=[0, None])
    mocker.patch.object(transformer, '_emulate_yield_from', return_value=[ast.Expr(value=ast.Name(id='test', ctx=ast.Load()))])
    
    # Creating a mock node with a body containing an ast.Assign node with ast.YieldFrom value
    node = ast.Module(body=[
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load())))
    ])
    
    # Call the method
    result = transformer._handle_assignments(node)
    
    # Assertions to verify the postconditions
    assert len(result.body) == 1
    assert isinstance(result.body[0], ast.Expr)
    assert result.body[0].value.id == 'test'
    assert transformer._tree_changed

    # Clean up
    mocker.stopall()
