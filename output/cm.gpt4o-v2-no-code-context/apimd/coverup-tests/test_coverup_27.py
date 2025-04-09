# file: apimd/parser.py:341-379
# asked: {"lines": [341, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [356, 368], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [373, 375], [375, 376], [375, 377], [377, 0], [377, 378], [378, 377], [378, 379]]}
# gained: {"lines": [341, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [356, 368], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [375, 376], [375, 377], [377, 0], [377, 378], [378, 379]]}

import pytest
from unittest.mock import MagicMock
from apimd.parser import Parser
from dataclasses import dataclass
from ast import AnnAssign, Assign, Name, Constant, Tuple, List

@dataclass
class MockNode:
    target: Name = None
    value: any = None
    annotation: any = None
    targets: list = None
    type_comment: str = None
    elts: list = None

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})

def test_globals_annassign(parser, mocker):
    root = 'root'
    node = AnnAssign(
        target=Name(id='TEST', ctx=None),
        value=Constant(value=42),
        annotation=Constant(value='int'),
        simple=1
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    mocker.patch.object(parser, 'resolve', return_value='int')
    parser.globals(root, node)
    name = f'{root}.TEST'
    assert parser.alias[name] == '42'
    assert parser.root[name] == root
    assert parser.const[name] == 'int'

def test_globals_assign_with_type_comment(parser, mocker):
    root = 'root'
    node = Assign(
        targets=[Name(id='TEST', ctx=None)],
        value=Constant(value=42),
        type_comment='int'
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    parser.globals(root, node)
    name = f'{root}.TEST'
    assert parser.alias[name] == '42'
    assert parser.root[name] == root
    assert parser.const[name] == 'int'

def test_globals_assign_without_type_comment(parser, mocker):
    root = 'root'
    node = Assign(
        targets=[Name(id='TEST', ctx=None)],
        value=Constant(value=42)
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    mocker.patch('apimd.parser.const_type', return_value='int')
    parser.globals(root, node)
    name = f'{root}.TEST'
    assert parser.alias[name] == '42'
    assert parser.root[name] == root
    assert parser.const[name] == 'int'

def test_globals_all_filter(parser, mocker):
    root = 'root'
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=Tuple(elts=[Constant(value='TEST')])
    )
    parser.imp = {root: set()}
    parser.globals(root, node)
    assert f'{root}.TEST' in parser.imp[root]

def test_globals_no_match(parser):
    root = 'root'
    node = MockNode()
    parser.globals(root, node)
    assert not parser.alias
    assert not parser.root
    assert not parser.const
