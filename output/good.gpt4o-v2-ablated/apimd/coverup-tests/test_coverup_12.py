# file: apimd/parser.py:182-195
# asked: {"lines": [184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [184, 186], [186, 187], [186, 188], [188, 189], [188, 190], [190, 191], [190, 195], [192, 194], [192, 195]]}
# gained: {"lines": [184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195], "branches": [[184, 185], [184, 186], [186, 187], [186, 188], [188, 189], [188, 190], [190, 191], [190, 195], [192, 194], [192, 195]]}

import pytest
from ast import Constant, Tuple, List, Set, Dict, Call, Name, Attribute, expr
from apimd.parser import const_type

def test_const_type_constant():
    node = Constant(value=42)
    assert const_type(node) == 'int'

def test_const_type_tuple(monkeypatch):
    node = Tuple(elts=[Constant(value=1), Constant(value=2)])
    monkeypatch.setattr('apimd.parser._type_name', lambda x: 'tuple')
    monkeypatch.setattr('apimd.parser._e_type', lambda x: 'int')
    assert const_type(node) == 'tupleint'

def test_const_type_list(monkeypatch):
    node = List(elts=[Constant(value=1), Constant(value=2)])
    monkeypatch.setattr('apimd.parser._type_name', lambda x: 'list')
    monkeypatch.setattr('apimd.parser._e_type', lambda x: 'int')
    assert const_type(node) == 'listint'

def test_const_type_set(monkeypatch):
    node = Set(elts=[Constant(value=1), Constant(value=2)])
    monkeypatch.setattr('apimd.parser._type_name', lambda x: 'set')
    monkeypatch.setattr('apimd.parser._e_type', lambda x: 'int')
    assert const_type(node) == 'setint'

def test_const_type_dict(monkeypatch):
    node = Dict(keys=[Constant(value=1)], values=[Constant(value='a')])
    monkeypatch.setattr('apimd.parser._e_type', lambda x, y: 'intstr')
    assert const_type(node) == 'dictintstr'

def test_const_type_call_name(monkeypatch):
    node = Call(func=Name(id='int', ctx=None), args=[], keywords=[])
    monkeypatch.setattr('apimd.parser.unparse', lambda x: 'int')
    assert const_type(node) == 'int'

def test_const_type_call_attribute(monkeypatch):
    node = Call(func=Attribute(value=Name(id='math', ctx=None), attr='sqrt', ctx=None), args=[], keywords=[])
    monkeypatch.setattr('apimd.parser.unparse', lambda x: 'math.sqrt')
    assert const_type(node) == 'Any'

def test_const_type_default():
    node = expr()
    assert const_type(node) == 'Any'
