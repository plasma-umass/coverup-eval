# file py_backwards/transformers/yield_from.py:43-53
# lines [45, 46, 47, 49, 51, 52, 53]
# branches ['46->47', '46->49']

import pytest
import ast
from py_backwards.transformers.yield_from import YieldFromTransformer
from py_backwards.transformers.base import BaseNodeTransformer

class MockTree:
    pass

@pytest.fixture
def transformer():
    tree = MockTree()
    return YieldFromTransformer(tree)

def test_emulate_yield_from_with_target(mocker, transformer):
    node = ast.YieldFrom(value=ast.Name(id='generator', ctx=ast.Load()))
    target = ast.Name(id='target', ctx=ast.Store())

    mocker.patch('py_backwards.transformers.yield_from.VariablesGenerator.generate', return_value='exc')
    mock_result_assignment = mocker.patch('py_backwards.transformers.yield_from.result_assignment.get_body', return_value=['assignment'])
    mock_yield_from = mocker.patch('py_backwards.transformers.yield_from.yield_from.get_body', return_value=['yield_from_body'])

    result = transformer._emulate_yield_from(target, node)

    mock_result_assignment.assert_called_once_with(exc='exc', target=target)
    mock_yield_from.assert_called_once_with(generator=node.value, assignment=['assignment'], exc='exc')
    assert result == ['yield_from_body']

def test_emulate_yield_from_without_target(mocker, transformer):
    node = ast.YieldFrom(value=ast.Name(id='generator', ctx=ast.Load()))

    mocker.patch('py_backwards.transformers.yield_from.VariablesGenerator.generate', return_value='exc')
    mock_yield_from = mocker.patch('py_backwards.transformers.yield_from.yield_from.get_body', return_value=['yield_from_body'])

    result = transformer._emulate_yield_from(None, node)

    mock_yield_from.assert_called_once_with(generator=node.value, assignment=[], exc='exc')
    assert result == ['yield_from_body']
