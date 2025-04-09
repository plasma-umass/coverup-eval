# file: apimd/parser.py:341-379
# asked: {"lines": [341, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [356, 368], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [373, 375], [375, 376], [375, 377], [377, 0], [377, 378], [378, 377], [378, 379]]}
# gained: {"lines": [341, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379], "branches": [[348, 353], [348, 356], [356, 361], [363, 364], [363, 366], [371, 372], [371, 375], [373, 374], [375, 376], [375, 377], [377, 0], [377, 378], [378, 379]]}

import pytest
from unittest.mock import MagicMock
from ast import AnnAssign, Assign, Name, Constant, Tuple, List
from apimd.parser import Parser, _m, const_type, ANY

@pytest.fixture
def parser():
    return Parser()

def test_globals_annassign(parser, mocker):
    node = AnnAssign(
        target=Name(id='MY_CONSTANT', ctx=None),
        annotation=Name(id='int', ctx=None),
        value=Constant(value=42),
        simple=1
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    mocker.patch.object(parser, 'resolve', return_value='int')
    
    parser.globals('root', node)
    
    name = _m('root', 'MY_CONSTANT')
    assert parser.alias[name] == '42'
    assert parser.root[name] == 'root'
    assert parser.const[name] == 'int'

def test_globals_assign(parser, mocker):
    node = Assign(
        targets=[Name(id='my_var', ctx=None)],
        value=Constant(value=42),
        type_comment=None
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    mocker.patch('apimd.parser.const_type', return_value='int')
    
    parser.globals('root', node)
    
    name = _m('root', 'my_var')
    assert parser.alias[name] == '42'
    assert name not in parser.root
    assert name not in parser.const

def test_globals_assign_with_type_comment(parser, mocker):
    node = Assign(
        targets=[Name(id='my_var', ctx=None)],
        value=Constant(value=42),
        type_comment='int'
    )
    mocker.patch('apimd.parser.unparse', return_value='42')
    
    parser.globals('root', node)
    
    name = _m('root', 'my_var')
    assert parser.alias[name] == '42'
    assert name not in parser.root
    assert name not in parser.const

def test_globals_all_filter(parser, mocker):
    node = Assign(
        targets=[Name(id='__all__', ctx=None)],
        value=List(elts=[Constant(value='my_var')], ctx=None),
        type_comment=None
    )
    mocker.patch('apimd.parser.unparse', return_value="['my_var']")
    
    if 'root' not in parser.imp:
        parser.imp['root'] = set()
    
    parser.globals('root', node)
    
    assert _m('root', 'my_var') in parser.imp['root']

def test_globals_no_match(parser):
    node = Assign(
        targets=[Name(id='my_var', ctx=None)],
        value=Constant(value=None),
        type_comment=None
    )
    
    result = parser.globals('root', node)
    
    assert result is None
