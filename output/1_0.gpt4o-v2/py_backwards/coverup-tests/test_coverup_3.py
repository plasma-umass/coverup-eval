# file: py_backwards/transformers/class_without_bases.py:5-20
# asked: {"lines": [5, 6, 13, 15, 16, 17, 18, 20], "branches": [[16, 17], [16, 20]]}
# gained: {"lines": [5, 6, 13, 15, 16, 17, 18, 20], "branches": [[16, 17], [16, 20]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.class_without_bases import ClassWithoutBasesTransformer

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return ClassWithoutBasesTransformer(tree)

def test_class_without_bases(transformer):
    node = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[])
    transformer.visit_ClassDef(node)
    assert len(node.bases) == 1
    assert isinstance(node.bases[0], ast.Name)
    assert node.bases[0].id == 'object'
    assert transformer._tree_changed

def test_class_with_bases(transformer):
    base = ast.Name(id='Base')
    node = ast.ClassDef(name='A', bases=[base], keywords=[], body=[], decorator_list=[])
    transformer.visit_ClassDef(node)
    assert len(node.bases) == 1
    assert node.bases[0] == base
    assert not transformer._tree_changed
