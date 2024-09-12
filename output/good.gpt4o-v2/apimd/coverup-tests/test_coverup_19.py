# file: apimd/parser.py:161-179
# asked: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}
# gained: {"lines": [161, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179], "branches": [[163, 164], [163, 165], [166, 167], [166, 179], [167, 168], [167, 169], [170, 171], [170, 178], [171, 172], [171, 173], [174, 175], [174, 177]]}

import pytest
from ast import Constant

from apimd.parser import _e_type

def test_e_type_no_elements():
    assert _e_type() == ''

def test_e_type_single_empty_element():
    assert _e_type([]) == ''

def test_e_type_single_none_element():
    assert _e_type([None]) == ''

def test_e_type_single_constant_element():
    element = [Constant(value=42)]
    assert _e_type(element) == '[int]'

def test_e_type_mixed_constant_elements():
    element1 = [Constant(value=42)]
    element2 = [Constant(value="string")]
    assert _e_type(element1, element2) == '[int, str]'

def test_e_type_non_constant_element():
    class NonConstant:
        pass
    element = [NonConstant()]
    assert _e_type(element) == ''

def test_e_type_mixed_types_in_single_element():
    element = [Constant(value=42), Constant(value="string")]
    assert _e_type(element) == '[Any]'

def test_e_type_multiple_elements_with_same_type():
    element1 = [Constant(value=42)]
    element2 = [Constant(value=100)]
    assert _e_type(element1, element2) == '[int, int]'

def test_e_type_multiple_elements_with_different_types():
    element1 = [Constant(value=42)]
    element2 = [Constant(value="string")]
    element3 = [Constant(value=3.14)]
    assert _e_type(element1, element2, element3) == '[int, str, float]'
