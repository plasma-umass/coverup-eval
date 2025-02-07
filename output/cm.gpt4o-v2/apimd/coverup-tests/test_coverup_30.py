# file: apimd/parser.py:513-516
# asked: {"lines": [515, 516], "branches": []}
# gained: {"lines": [515, 516], "branches": []}

import pytest
from unittest.mock import MagicMock
from ast import Name, Subscript, Attribute, Constant
from apimd.parser import Parser, Resolver

@pytest.fixture
def parser():
    return Parser()

def test_resolve_with_name_node(parser, mocker):
    mocker.patch.object(Resolver, 'visit', return_value=Name(id='mocked_name', ctx=None))
    mocker.patch.object(Resolver, 'generic_visit', return_value=Name(id='mocked_name', ctx=None))
    mocker.patch('apimd.parser.unparse', return_value='mocked_name')

    node = Name(id='test', ctx=None)
    result = parser.resolve('root', node, 'self_ty')

    assert result == 'mocked_name'

def test_resolve_with_subscript_node(parser, mocker):
    mocker.patch.object(Resolver, 'visit', return_value=Subscript(value=Name(id='mocked_name', ctx=None), slice=Constant(value='mocked_slice'), ctx=None))
    mocker.patch.object(Resolver, 'generic_visit', return_value=Subscript(value=Name(id='mocked_name', ctx=None), slice=Constant(value='mocked_slice'), ctx=None))
    mocker.patch('apimd.parser.unparse', return_value='mocked_subscript')

    node = Subscript(value=Name(id='test', ctx=None), slice=Constant(value='slice'), ctx=None)
    result = parser.resolve('root', node, 'self_ty')

    assert result == 'mocked_subscript'

def test_resolve_with_attribute_node(parser, mocker):
    mocker.patch.object(Resolver, 'visit', return_value=Attribute(value=Name(id='mocked_name', ctx=None), attr='mocked_attr', ctx=None))
    mocker.patch.object(Resolver, 'generic_visit', return_value=Attribute(value=Name(id='mocked_name', ctx=None), attr='mocked_attr', ctx=None))
    mocker.patch('apimd.parser.unparse', return_value='mocked_attribute')

    node = Attribute(value=Name(id='test', ctx=None), attr='attr', ctx=None)
    result = parser.resolve('root', node, 'self_ty')

    assert result == 'mocked_attribute'
