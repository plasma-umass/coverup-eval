# file: py_backwards/transformers/metaclass.py:17-40
# asked: {"lines": [17, 18, 25, 26, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40], "branches": [[33, 34], [33, 40]]}
# gained: {"lines": [17, 18, 25, 26, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40], "branches": [[33, 34], [33, 40]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.metaclass import MetaclassTransformer
from py_backwards.utils.tree import insert_at
from py_backwards.transformers.base import BaseNodeTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return MetaclassTransformer(tree)

def test_visit_module(transformer, mocker):
    node = ast.Module(body=[])
    mock_six_import = mocker.patch('py_backwards.transformers.metaclass.six_import')
    mock_six_import.get_body.return_value = [ast.Import(names=[ast.alias(name='six', asname=None)])]

    result = transformer.visit_Module(node)

    assert len(result.body) == 1
    assert isinstance(result.body[0], ast.Import)
    assert result.body[0].names[0].name == 'six'

def test_visit_classdef_with_metaclass(transformer, mocker):
    metaclass = ast.Name(id='Meta', ctx=ast.Load())
    node = ast.ClassDef(name='A', bases=[], keywords=[ast.keyword(arg='metaclass', value=metaclass)], body=[], decorator_list=[])
    mock_class_bases = mocker.patch('py_backwards.transformers.metaclass.class_bases')
    mock_class_bases.get_body.return_value = [ast.Name(id='_py_backwards_six_with_metaclass', ctx=ast.Load())]

    result = transformer.visit_ClassDef(node)

    assert len(result.bases) == 1
    assert result.bases[0].id == '_py_backwards_six_with_metaclass'
    assert result.keywords == []
    assert transformer._tree_changed

def test_visit_classdef_without_metaclass(transformer):
    node = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[])

    result = transformer.visit_ClassDef(node)

    assert result == node
