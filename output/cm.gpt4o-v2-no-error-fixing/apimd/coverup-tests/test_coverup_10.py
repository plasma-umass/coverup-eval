# file: apimd/parser.py:161-179
# asked: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}
# gained: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}

import pytest
from ast import Constant
from apimd.parser import _e_type

def test_e_type_no_elements():
    assert _e_type() == ""

def test_e_type_none_element():
    assert _e_type(None) == ""

def test_e_type_non_constant_element():
    class NonConstant:
        pass
    assert _e_type([NonConstant()]) == ""

def test_e_type_mixed_constants():
    assert _e_type([Constant(1), Constant("string")]) == "[Any]"

def test_e_type_same_constants():
    assert _e_type([Constant(1), Constant(2)]) == "[int]"

def test_e_type_different_constants():
    assert _e_type([Constant(1)], [Constant("string")]) == "[int, str]"

