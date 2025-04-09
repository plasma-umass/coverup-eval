# file: apimd/parser.py:182-195
# asked: {"lines": [185, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [186, 188], [188, 189], [188, 190], [190, 191], [190, 195], [192, 194], [192, 195]]}
# gained: {"lines": [185, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [186, 188], [188, 189], [188, 190], [190, 191], [192, 194], [192, 195]]}

import pytest
from ast import Constant, Tuple, List, Set, Dict, Call, Name, Attribute
from apimd.parser import const_type, _type_name, _e_type, unparse, PEP585, ANY

def test_const_type_constant():
    node = Constant(value=42)
    assert const_type(node) == _type_name(42)

def test_const_type_tuple():
    node = Tuple(elts=[Constant(value=1), Constant(value=2)], ctx=None)
    assert const_type(node) == _type_name(node).lower() + _e_type(node.elts)

def test_const_type_list():
    node = List(elts=[Constant(value=1), Constant(value=2)], ctx=None)
    assert const_type(node) == _type_name(node).lower() + _e_type(node.elts)

def test_const_type_set():
    node = Set(elts=[Constant(value=1), Constant(value=2)])
    assert const_type(node) == _type_name(node).lower() + _e_type(node.elts)

def test_const_type_dict():
    node = Dict(keys=[Constant(value='key')], values=[Constant(value='value')])
    assert const_type(node) == 'dict' + _e_type(node.keys, node.values)

def test_const_type_call():
    node = Call(func=Name(id='int', ctx=None), args=[], keywords=[])
    assert const_type(node) == 'int'

    node = Call(func=Name(id='custom_func', ctx=None), args=[], keywords=[])
    assert const_type(node) == ANY

def test_const_type_call_attribute():
    node = Call(func=Attribute(value=Name(id='module', ctx=None), attr='int', ctx=None), args=[], keywords=[])
    assert const_type(node) == ANY

    node = Call(func=Attribute(value=Name(id='module', ctx=None), attr='custom_func', ctx=None), args=[], keywords=[])
    assert const_type(node) == ANY
