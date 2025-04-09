# file: apimd/parser.py:341-379
# asked: {"lines": [348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [356, 368], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [373, 375], [375, 376], [375, 377], [377, 0], [377, 378], [378, 377], [378, 379]]}
# gained: {"lines": [348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [375, 376], [375, 377], [377, 0], [377, 378], [378, 379]]}

import pytest
from ast import AnnAssign, Assign, Name, Constant, Tuple, List
from apimd.parser import Parser, _m, const_type

@pytest.fixture
def parser():
    return Parser()

def test_globals_annassign(parser, mocker):
    node = AnnAssign(
        target=Name(id='TEST', ctx=None),
        annotation=Name(id='int', ctx=None),
        value=Constant(value=42),
        simple=1
    )
    mocker.patch.object(parser, 'resolve', return_value='int')
    parser.globals('root', node)
    name = _m('root', 'TEST')
    assert parser.alias[name] == '42'
    assert parser.root[name] == 'root'
    assert parser.const[name] == 'int'

def test_globals_assign_with_type_comment(parser, mocker):
    node = Assign(
        targets=[Name(id='TEST', ctx=None)],
        value=Constant(value=42),
        type_comment='int'
    )
    parser.globals('root', node)
    name = _m('root', 'TEST')
    assert parser.alias[name] == '42'
    assert parser.root[name] == 'root'
    assert parser.const[name] == 'int'

def test_globals_assign_without_type_comment(parser, mocker):
    node = Assign(
        targets=[Name(id='TEST', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    parser.globals('root', node)
    name = _m('root', 'TEST')
    assert parser.alias[name] == '42'
    assert parser.root[name] == 'root'
    assert parser.const[name] == const_type(node.value)

def test_globals_all_filter(parser, mocker):
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=List(elts=[Constant(value='TEST')], ctx=None),
        type_comment=None
    )
    parser.imp = {'root': set()}
    parser.globals('root', node)
    assert _m('root', 'TEST') in parser.imp['root']
