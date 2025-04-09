# file apimd/parser.py:341-379
# lines [341, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 361, 362, 363, 364, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379]
# branches ['348->353', '348->356', '356->361', '356->368', '363->364', '363->366', '371->372', '371->375', '373->374', '373->375', '375->376', '375->377', '377->exit', '377->378', '378->377', '378->379']

import pytest
from apimd.parser import Parser
from ast import AnnAssign, Assign, Name, Constant, Tuple, List, parse

@pytest.fixture
def parser():
    return Parser()

def test_parser_globals_annassign_uppercase(parser, mocker):
    mocker.patch('apimd.parser.unparse', return_value='expression')
    mocker.patch('apimd.parser.const_type', return_value='const_type')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    mocker.patch('apimd.parser.Parser.resolve', return_value='resolved_annotation')

    root = 'root'
    node = AnnAssign(target=Name(id='CONSTANT', ctx=None), annotation=None, value=Constant(value='value'), simple=1)
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {root: set()}

    parser.globals(root, node)

    assert parser.alias == {f'{root}.CONSTANT': 'expression'}
    assert parser.root == {f'{root}.CONSTANT': root}
    assert parser.const == {f'{root}.CONSTANT': 'resolved_annotation'}
    assert parser.imp == {root: set()}

def test_parser_globals_assign_with_type_comment(parser, mocker):
    mocker.patch('apimd.parser.unparse', return_value='expression')
    mocker.patch('apimd.parser.const_type', return_value='const_type')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    mocker.patch('apimd.parser.Parser.resolve', return_value='resolved_annotation')

    root = 'root'
    node = Assign(targets=[Name(id='variable', ctx=None)], value=Constant(value='value'), type_comment='type_comment')
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {root: set()}

    parser.globals(root, node)

    assert parser.alias == {f'{root}.variable': 'expression'}
    assert parser.root == {}
    assert parser.const == {}
    assert parser.imp == {root: set()}

def test_parser_globals_assign_with_const_type(parser, mocker):
    mocker.patch('apimd.parser.unparse', return_value='expression')
    mocker.patch('apimd.parser.const_type', return_value='const_type')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    mocker.patch('apimd.parser.Parser.resolve', return_value='resolved_annotation')

    root = 'root'
    node = Assign(targets=[Name(id='variable', ctx=None)], value=Constant(value='value'), type_comment=None)
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {root: set()}

    parser.globals(root, node)

    assert parser.alias == {f'{root}.variable': 'expression'}
    assert parser.root == {}
    assert parser.const == {}
    assert parser.imp == {root: set()}

def test_parser_globals_assign_with_all_list(parser, mocker):
    mocker.patch('apimd.parser.unparse', return_value='expression')
    mocker.patch('apimd.parser.const_type', return_value='const_type')
    mocker.patch('apimd.parser._m', side_effect=lambda root, id: f'{root}.{id}')
    mocker.patch('apimd.parser.Parser.resolve', return_value='resolved_annotation')

    root = 'root'
    node = Assign(targets=[Name(id='__all__', ctx=None)], value=List(elts=[Constant(value='value1'), Constant(value='value2')]), type_comment=None)
    parser.alias = {}
    parser.root = {}
    parser.const = {}
    parser.imp = {root: set()}

    parser.globals(root, node)

    assert parser.alias == {f'{root}.__all__': 'expression'}
    assert parser.root == {}
    assert parser.const == {}
    assert parser.imp == {root: {f'{root}.value1', f'{root}.value2'}}
