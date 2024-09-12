# file: py_backwards/transformers/dict_unpacking.py:59-65
# asked: {"lines": [59, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [59, 62, 63, 64, 65], "branches": []}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

def test_merge_dicts():
    # Create a sample AST tree
    tree = ast.Module(body=[])
    
    # Initialize the transformer with the tree
    transformer = DictUnpackingTransformer(tree)
    
    # Create sample input
    dict1 = ast.Dict(keys=[], values=[])
    dict2 = ast.Dict(keys=[], values=[])
    call1 = ast.Call(func=ast.Name(id='func1'), args=[], keywords=[])
    
    # Call the method
    result = transformer._merge_dicts([dict1, dict2, call1])
    
    # Assertions to verify the result
    assert isinstance(result, ast.Call)
    assert isinstance(result.func, ast.Name)
    assert result.func.id == '_py_backwards_merge_dicts'
    assert isinstance(result.args, list)
    assert len(result.args) == 1
    assert isinstance(result.args[0], ast.List)
    assert result.args[0].elts == [dict1, dict2, call1]
    assert result.keywords == []
