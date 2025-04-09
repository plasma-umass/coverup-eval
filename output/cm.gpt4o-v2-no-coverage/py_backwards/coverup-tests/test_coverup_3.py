# file: py_backwards/transformers/string_types.py:7-22
# asked: {"lines": [7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19]]}
# gained: {"lines": [7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 22], [18, 17], [18, 19]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.string_types import StringTypesTransformer
from py_backwards.types import TransformationResult

def test_string_types_transformer_transform():
    # Create a sample AST with a 'str' node
    tree = ast.parse("a = str('test')")
    
    # Transform the tree
    result = StringTypesTransformer.transform(tree)
    
    # Check that the tree was changed
    assert result.tree_changed is True
    
    # Check that 'str' was replaced with 'unicode'
    assert isinstance(result.tree.body[0].value, ast.Call)
    assert isinstance(result.tree.body[0].value.func, ast.Name)
    assert result.tree.body[0].value.func.id == 'unicode'

def test_string_types_transformer_no_change():
    # Create a sample AST without a 'str' node
    tree = ast.parse("a = int('test')")
    
    # Transform the tree
    result = StringTypesTransformer.transform(tree)
    
    # Check that the tree was not changed
    assert result.tree_changed is False
    
    # Check that 'int' was not replaced
    assert isinstance(result.tree.body[0].value, ast.Call)
    assert isinstance(result.tree.body[0].value.func, ast.Name)
    assert result.tree.body[0].value.func.id == 'int'
