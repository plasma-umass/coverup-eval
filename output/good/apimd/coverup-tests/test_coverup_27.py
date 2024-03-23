# file apimd/parser.py:182-195
# lines [182, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195]
# branches ['184->185', '184->186', '186->187', '186->188', '188->189', '188->190', '190->191', '190->195', '192->194', '192->195']

import pytest
from apimd.parser import const_type
from ast import Constant, Tuple, List, Set, Dict, Call, Name, Load

# Assuming _type_name, _e_type, PEP585, and ANY are defined elsewhere in apimd.parser
# If not, they should be mocked or defined for testing purposes.

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup code if necessary

def test_const_type_with_constant(cleanup):
    node = Constant(value=1)
    assert const_type(node) == 'int'

def test_const_type_with_tuple(cleanup, mocker):
    mocker.patch('apimd.parser._type_name', return_value='Tuple')
    mocker.patch('apimd.parser._e_type', return_value='<elts>')
    node = Tuple(elts=[Constant(value=1)], ctx=Load())
    assert const_type(node) == 'tuple<elts>'

def test_const_type_with_list(cleanup, mocker):
    mocker.patch('apimd.parser._type_name', return_value='List')
    mocker.patch('apimd.parser._e_type', return_value='<elts>')
    node = List(elts=[Constant(value=1)], ctx=Load())
    assert const_type(node) == 'list<elts>'

def test_const_type_with_set(cleanup, mocker):
    mocker.patch('apimd.parser._type_name', return_value='Set')
    mocker.patch('apimd.parser._e_type', return_value='<elts>')
    node = Set(elts=[Constant(value=1)], ctx=Load())
    assert const_type(node) == 'set<elts>'

def test_const_type_with_dict(cleanup, mocker):
    mocker.patch('apimd.parser._type_name', return_value='Dict')
    mocker.patch('apimd.parser._e_type', return_value='<keys_values>')
    node = Dict(keys=[Constant(value=1)], values=[Constant(value=2)])
    assert const_type(node) == 'dict<keys_values>'

def test_const_type_with_call(cleanup, mocker):
    mocker.patch('apimd.parser.unparse', return_value='int')
    mocker.patch('apimd.parser.PEP585', return_value={'int': 'int'})
    node = Call(func=Name(id='int', ctx=Load()), args=[], keywords=[])
    assert const_type(node) == 'int'

def test_const_type_with_unrecognized_call(cleanup, mocker):
    mocker.patch('apimd.parser.unparse', return_value='unrecognized_func')
    mocker.patch('apimd.parser.PEP585', return_value={'int': 'int'})
    mocker.patch('apimd.parser.ANY', 'Any')
    node = Call(func=Name(id='unrecognized_func', ctx=Load()), args=[], keywords=[])
    assert const_type(node) == 'Any'
