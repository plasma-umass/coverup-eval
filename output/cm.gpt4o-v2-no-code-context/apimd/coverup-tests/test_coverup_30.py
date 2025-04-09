# file: apimd/parser.py:341-379
# asked: {"lines": [], "branches": [[373, 375], [378, 377]]}
# gained: {"lines": [], "branches": [[378, 377]]}

import pytest
from unittest.mock import MagicMock
from apimd.parser import Parser
from ast import AnnAssign, Assign, Name, Constant, Tuple, List

@pytest.fixture
def parser():
    return Parser()

def test_globals_annassign(parser, mocker):
    node = AnnAssign(
        target=Name(id='CONSTANT', ctx=None),
        annotation=None,
        value=Constant(value=42),
        simple=1
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.resolve = mocker.MagicMock(return_value='int')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.globals('root', node)
    assert parser.alias['root.CONSTANT'] == '42'
    assert parser.root['root.CONSTANT'] == 'root'
    assert parser.const['root.CONSTANT'] == 'int'

def test_globals_assign_with_type_comment(parser, mocker):
    node = Assign(
        targets=[Name(id='CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment='int'
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.globals('root', node)
    assert parser.alias['root.CONSTANT'] == '42'
    assert parser.root['root.CONSTANT'] == 'root'
    assert parser.const['root.CONSTANT'] == 'int'

def test_globals_assign_without_type_comment(parser, mocker):
    node = Assign(
        targets=[Name(id='CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    mocker.patch('apimd.parser.const_type', return_value='int')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.globals('root', node)
    assert parser.alias['root.CONSTANT'] == '42'
    assert parser.root['root.CONSTANT'] == 'root'
    assert parser.const['root.CONSTANT'] == 'int'

def test_globals_all(parser, mocker):
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=List(elts=[Constant(value='func1'), Constant(value='func2')], ctx=None),
        type_comment=None
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {'root': set()}
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.globals('root', node)
    assert 'root.func1' in parser.imp['root']
    assert 'root.func2' in parser.imp['root']

def test_globals_const_any(parser, mocker):
    node = Assign(
        targets=[Name(id='CONSTANT', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    mocker.patch('apimd.parser.const_type', return_value='int')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.const = {}
    parser.globals('root', node)
    assert parser.const['root.CONSTANT'] == 'int'

def test_globals_all_with_non_string_elements(parser, mocker):
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=List(elts=[Constant(value=1), Constant(value=2)], ctx=None),
        type_comment=None
    )
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {'root': set()}
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    parser.globals('root', node)
    assert 'root.1' not in parser.imp['root']
    assert 'root.2' not in parser.imp['root']
