# file: py_backwards/transformers/dict_unpacking.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.utils.tree import insert_at

@pytest.fixture
def mock_merge_dicts(mocker):
    mock_merge_dicts = mocker.patch('py_backwards.transformers.dict_unpacking.merge_dicts')
    mock_merge_dicts.get_body.return_value = [ast.Expr(value=ast.Str(s='test'))]
    return mock_merge_dicts

def test_visit_module(monkeypatch, mock_merge_dicts):
    tree = ast.Module(body=[])
    transformer = DictUnpackingTransformer(tree)
    module_node = ast.Module(body=[])
    
    result_node = transformer.visit_Module(module_node)
    
    assert len(result_node.body) == 1
    assert isinstance(result_node.body[0], ast.Expr)
    assert result_node.body[0].value.s == 'test'

def test_insert_at():
    parent_node = ast.Module(body=[])
    child_node = ast.Expr(value=ast.Str(s='test'))
    
    insert_at(0, parent_node, child_node)
    
    assert len(parent_node.body) == 1
    assert parent_node.body[0] == child_node

    # Test inserting a list of nodes
    another_child_node = ast.Expr(value=ast.Str(s='another_test'))
    insert_at(1, parent_node, [another_child_node])
    
    assert len(parent_node.body) == 2
    assert parent_node.body[1] == another_child_node
