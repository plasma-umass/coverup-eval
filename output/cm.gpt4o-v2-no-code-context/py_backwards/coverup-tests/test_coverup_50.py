# file: py_backwards/transformers/metaclass.py:17-40
# asked: {"lines": [29, 30, 33, 34, 35, 36, 37, 38, 40], "branches": [[33, 34], [33, 40]]}
# gained: {"lines": [29, 30, 33, 34, 35, 36, 37, 38, 40], "branches": [[33, 34], [33, 40]]}

import ast
import pytest
from py_backwards.transformers.metaclass import MetaclassTransformer

class MockSixImport:
    @staticmethod
    def get_body():
        return [ast.Import(names=[ast.alias(name='six', asname=None)])]

class MockClassBases:
    @staticmethod
    def get_body(metaclass, bases):
        return [ast.Call(func=ast.Name(id='_py_backwards_six_with_metaclass', ctx=ast.Load()),
                         args=[metaclass], keywords=[])]

@pytest.fixture
def mock_six_import(monkeypatch):
    monkeypatch.setattr('py_backwards.transformers.metaclass.six_import', MockSixImport)

@pytest.fixture
def mock_class_bases(monkeypatch):
    monkeypatch.setattr('py_backwards.transformers.metaclass.class_bases', MockClassBases)

def test_visit_module(mock_six_import):
    transformer = MetaclassTransformer(tree=None)
    module_node = ast.Module(body=[])
    transformed_node = transformer.visit_Module(module_node)

    assert isinstance(transformed_node, ast.Module)
    assert isinstance(transformed_node.body[0], ast.Import)
    assert transformed_node.body[0].names[0].name == 'six'

def test_visit_classdef_with_keywords(mock_class_bases):
    transformer = MetaclassTransformer(tree=None)
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[],
        decorator_list=[]
    )
    transformed_node = transformer.visit_ClassDef(class_node)

    assert isinstance(transformed_node, ast.ClassDef)
    assert len(transformed_node.bases) == 1
    assert isinstance(transformed_node.bases[0], ast.Call)
    assert transformed_node.bases[0].func.id == '_py_backwards_six_with_metaclass'
    assert transformed_node.bases[0].args[0].id == 'B'
    assert transformed_node.keywords == []
    assert transformer._tree_changed

def test_visit_classdef_without_keywords():
    transformer = MetaclassTransformer(tree=None)
    class_node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[]
    )
    transformed_node = transformer.visit_ClassDef(class_node)

    assert isinstance(transformed_node, ast.ClassDef)
    assert transformed_node.bases == []
    assert transformed_node.keywords == []
