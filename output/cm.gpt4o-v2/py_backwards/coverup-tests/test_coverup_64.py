# file: py_backwards/transformers/yield_from.py:43-53
# asked: {"lines": [45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}
# gained: {"lines": [45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.utils.helpers import VariablesGenerator

@pytest.fixture
def reset_variable_generator_counter():
    original_counter = VariablesGenerator._counter
    yield
    VariablesGenerator._counter = original_counter

def test_emulate_yield_from_with_target(reset_variable_generator_counter):
    tree = ast.Module(body=[])
    transformer = YieldFromTransformer(tree)
    target = ast.Name(id='target', ctx=ast.Store())
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    
    result = transformer._emulate_yield_from(target, node)
    
    assert isinstance(result, list)
    assert len(result) > 0
    assert VariablesGenerator._counter > 0

def test_emulate_yield_from_without_target(reset_variable_generator_counter):
    tree = ast.Module(body=[])
    transformer = YieldFromTransformer(tree)
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    
    result = transformer._emulate_yield_from(None, node)
    
    assert isinstance(result, list)
    assert len(result) > 0
    assert VariablesGenerator._counter > 0
