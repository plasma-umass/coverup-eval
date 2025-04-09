# file: apimd/parser.py:513-516
# asked: {"lines": [513, 515, 516], "branches": []}
# gained: {"lines": [513, 515, 516], "branches": []}

import pytest
from ast import parse, Name, Constant
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})

def test_resolve_with_name(parser):
    node = Name(id='test', ctx=None)
    result = parser.resolve('root', node)
    assert isinstance(result, str)
    assert 'test' in result

def test_resolve_with_constant(parser):
    node = Constant(value='test')
    result = parser.resolve('root', node)
    assert isinstance(result, str)
    assert 'test' in result

def test_resolve_with_empty_self_ty(parser):
    node = Name(id='test', ctx=None)
    result = parser.resolve('root', node, self_ty='')
    assert isinstance(result, str)
    assert 'test' in result

def test_resolve_with_non_empty_self_ty(parser):
    node = Name(id='test', ctx=None)
    result = parser.resolve('root', node, self_ty='self_type')
    assert isinstance(result, str)
    assert 'test' in result
