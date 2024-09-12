# file: apimd/parser.py:182-195
# asked: {"lines": [185, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [186, 188], [188, 189], [188, 190], [190, 191], [190, 195], [192, 194], [192, 195]]}
# gained: {"lines": [185, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [186, 188], [188, 189], [188, 190], [190, 191], [190, 195], [192, 194]]}

import pytest
from ast import Constant, Tuple, List, Set, Dict, Call, Name, Attribute
from apimd.parser import const_type

def test_const_type_with_constant():
    node = Constant(value=42)
    assert const_type(node) == 'int'

def test_const_type_with_tuple():
    node = Tuple(elts=[Constant(value=1), Constant(value=2)], ctx=None)
    assert const_type(node) == 'tuple[int]'

def test_const_type_with_list():
    node = List(elts=[Constant(value=1), Constant(value=2)], ctx=None)
    assert const_type(node) == 'list[int]'

def test_const_type_with_set():
    node = Set(elts=[Constant(value=1), Constant(value=2)])
    assert const_type(node) == 'set[int]'

def test_const_type_with_dict():
    node = Dict(keys=[Constant(value=1)], values=[Constant(value='a')])
    assert const_type(node) == 'dict[int, str]'

def test_const_type_with_call_name():
    node = Call(func=Name(id='int', ctx=None), args=[], keywords=[])
    assert const_type(node) == 'int'

def test_const_type_with_call_attribute():
    node = Call(func=Attribute(value=Name(id='typing', ctx=None), attr='List', ctx=None), args=[], keywords=[])
    assert const_type(node) == 'typing.List'

def test_const_type_with_unknown():
    node = Name(id='unknown', ctx=None)
    assert const_type(node) == 'Any'
