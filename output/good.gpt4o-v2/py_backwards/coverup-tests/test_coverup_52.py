# file: py_backwards/transformers/dict_unpacking.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer
from py_backwards.utils.tree import insert_at

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return DictUnpackingTransformer(tree)

def test_visit_module_inserts_body(monkeypatch, transformer):
    class MockMergeDicts:
        @staticmethod
        def get_body():
            return [ast.Expr(value=ast.Str(s="test"))]

    monkeypatch.setattr("py_backwards.transformers.dict_unpacking.merge_dicts", MockMergeDicts)

    module_node = ast.Module(body=[])
    result_node = transformer.visit_Module(module_node)

    assert len(result_node.body) == 1
    assert isinstance(result_node.body[0], ast.Expr)
    assert isinstance(result_node.body[0].value, ast.Str)
    assert result_node.body[0].value.s == "test"

def test_insert_at():
    parent_node = ast.Module(body=[])
    new_node = ast.Expr(value=ast.Str(s="test"))

    insert_at(0, parent_node, new_node)

    assert len(parent_node.body) == 1
    assert isinstance(parent_node.body[0], ast.Expr)
    assert isinstance(parent_node.body[0].value, ast.Str)
    assert parent_node.body[0].value.s == "test"
