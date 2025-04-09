# file: apimd/parser.py:513-516
# asked: {"lines": [513, 515, 516], "branches": []}
# gained: {"lines": [513, 515, 516], "branches": []}

import pytest
from unittest.mock import MagicMock
from ast import Name, Subscript, Attribute, Constant
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_resolve_with_name(parser, monkeypatch):
    mock_resolver = MagicMock()
    monkeypatch.setattr('apimd.parser.Resolver', mock_resolver)
    
    node = Name(id='test', ctx=None)
    mock_resolver.return_value.visit.return_value = node
    mock_resolver.return_value.generic_visit.return_value = node
    
    result = parser.resolve('root', node)
    
    mock_resolver.assert_called_once_with('root', parser.alias, '')
    mock_resolver.return_value.visit.assert_called_once_with(node)
    mock_resolver.return_value.generic_visit.assert_called_once_with(node)
    assert result == 'test'

def test_resolve_with_subscript(parser, monkeypatch):
    mock_resolver = MagicMock()
    monkeypatch.setattr('apimd.parser.Resolver', mock_resolver)
    
    node = Subscript(value=Name(id='List', ctx=None), slice=Name(id='int', ctx=None), ctx=None)
    mock_resolver.return_value.visit.return_value = node
    mock_resolver.return_value.generic_visit.return_value = node
    
    result = parser.resolve('root', node)
    
    mock_resolver.assert_called_once_with('root', parser.alias, '')
    mock_resolver.return_value.visit.assert_called_once_with(node)
    mock_resolver.return_value.generic_visit.assert_called_once_with(node)
    assert result == 'List[int]'

def test_resolve_with_attribute(parser, monkeypatch):
    mock_resolver = MagicMock()
    monkeypatch.setattr('apimd.parser.Resolver', mock_resolver)
    
    node = Attribute(value=Name(id='module', ctx=None), attr='attr', ctx=None)
    mock_resolver.return_value.visit.return_value = node
    mock_resolver.return_value.generic_visit.return_value = node
    
    result = parser.resolve('root', node)
    
    mock_resolver.assert_called_once_with('root', parser.alias, '')
    mock_resolver.return_value.visit.assert_called_once_with(node)
    mock_resolver.return_value.generic_visit.assert_called_once_with(node)
    assert result == 'module.attr'

def test_resolve_with_constant(parser, monkeypatch):
    mock_resolver = MagicMock()
    monkeypatch.setattr('apimd.parser.Resolver', mock_resolver)
    
    node = Constant(value='test')
    mock_resolver.return_value.visit.return_value = node
    mock_resolver.return_value.generic_visit.return_value = node
    
    result = parser.resolve('root', node)
    
    mock_resolver.assert_called_once_with('root', parser.alias, '')
    mock_resolver.return_value.visit.assert_called_once_with(node)
    mock_resolver.return_value.generic_visit.assert_called_once_with(node)
    assert result == "'test'"
