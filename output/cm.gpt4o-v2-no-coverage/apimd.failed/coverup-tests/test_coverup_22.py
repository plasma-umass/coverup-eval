# file: apimd/parser.py:161-179
# asked: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}
# gained: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}

import pytest
from ast import Constant, Expr, List
from apimd.parser import _e_type

def test_e_type_no_elements():
    assert _e_type() == ""

def test_e_type_none_element():
    assert _e_type(None) == ""

def test_e_type_non_constant_element():
    expr = [Expr()]
    assert _e_type(expr) == ""

def test_e_type_single_constant_element():
    expr = [Constant(value=42)]
    assert _e_type(expr) == "[int]"

def test_e_type_mixed_constant_elements():
    expr1 = [Constant(value=42)]
    expr2 = [Constant(value="string")]
    assert _e_type(expr1, expr2) == "[int, str]"

def test_e_type_different_types_in_same_element():
    expr = [Constant(value=42), Constant(value="string")]
    assert _e_type(expr) == "[Any]"

def test_e_type_empty_element():
    expr = [[], []]
    assert _e_type(expr) == ""
