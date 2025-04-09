# file: py_backwards/transformers/yield_from.py:43-53
# asked: {"lines": [43, 45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}
# gained: {"lines": [43, 45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.utils.helpers import VariablesGenerator

@pytest.fixture
def mock_generate(mocker):
    mocker.patch.object(VariablesGenerator, 'generate', return_value='mocked_exc')
    yield
    VariablesGenerator.generate.assert_called()

@pytest.fixture
def transformer():
    tree = ast.Module(body=[])
    return YieldFromTransformer(tree)

def test_emulate_yield_from_with_target(transformer, mock_generate):
    target = ast.Name(id='target', ctx=ast.Store())
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    
    result = transformer._emulate_yield_from(target, node)
    
    assert isinstance(result, list)
    assert len(result) > 0

def test_emulate_yield_from_without_target(transformer, mock_generate):
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    
    result = transformer._emulate_yield_from(None, node)
    
    assert isinstance(result, list)
    assert len(result) > 0
