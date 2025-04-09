# file: py_backwards/transformers/string_types.py:7-22
# asked: {"lines": [7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19]]}
# gained: {"lines": [7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.string_types import StringTypesTransformer
from py_backwards.types import TransformationResult

def test_string_types_transformer_transform():
    # Create a sample AST tree with a 'str' node
    tree = ast.parse("a = str('test')")
    
    # Transform the tree
    result = StringTypesTransformer.transform(tree)
    
    # Check that the tree was changed
    assert result.tree_changed is True
    
    # Check that 'str' was replaced with 'unicode'
    assert isinstance(result.tree.body[0].value, ast.Call)
    assert result.tree.body[0].value.func.id == 'unicode'
    
    # Check that dependencies are empty
    assert result.dependencies == []

def test_string_types_transformer_no_change():
    # Create a sample AST tree without a 'str' node
    tree = ast.parse("a = unicode('test')")
    
    # Transform the tree
    result = StringTypesTransformer.transform(tree)
    
    # Check that the tree was not changed
    assert result.tree_changed is False
    
    # Check that the tree remains the same
    assert isinstance(result.tree.body[0].value, ast.Call)
    assert result.tree.body[0].value.func.id == 'unicode'
    
    # Check that dependencies are empty
    assert result.dependencies == []
