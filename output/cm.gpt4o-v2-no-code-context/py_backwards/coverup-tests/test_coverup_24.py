# file: py_backwards/transformers/yield_from.py:43-53
# asked: {"lines": [43, 45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}
# gained: {"lines": [43, 45, 46, 47, 49, 51, 52, 53], "branches": [[46, 47], [46, 49]]}

import pytest
import ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

@pytest.fixture
def transformer():
    return YieldFromTransformer(tree=MockTree())

def test_emulate_yield_from_with_target(transformer, mocker):
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    target = ast.Name(id='result', ctx=ast.Store())
    
    mock_generate = mocker.patch('py_backwards.transformers.yield_from.VariablesGenerator.generate', return_value='exc')
    mock_get_body = mocker.patch('py_backwards.transformers.yield_from.result_assignment.get_body', return_value=['assignment'])
    mock_yield_from_body = mocker.patch('py_backwards.transformers.yield_from.yield_from.get_body', return_value=['yield_from_body'])
    
    result = transformer._emulate_yield_from(target, node)
    
    mock_generate.assert_called_once_with('exc')
    mock_get_body.assert_called_once_with(exc='exc', target=target)
    mock_yield_from_body.assert_called_once_with(generator=node.value, assignment=['assignment'], exc='exc')
    
    assert result == ['yield_from_body']

def test_emulate_yield_from_without_target(transformer, mocker):
    node = ast.YieldFrom(value=ast.Name(id='gen', ctx=ast.Load()))
    target = None
    
    mock_generate = mocker.patch('py_backwards.transformers.yield_from.VariablesGenerator.generate', return_value='exc')
    mock_yield_from_body = mocker.patch('py_backwards.transformers.yield_from.yield_from.get_body', return_value=['yield_from_body'])
    
    result = transformer._emulate_yield_from(target, node)
    
    mock_generate.assert_called_once_with('exc')
    mock_yield_from_body.assert_called_once_with(generator=node.value, assignment=[], exc='exc')
    
    assert result == ['yield_from_body']
