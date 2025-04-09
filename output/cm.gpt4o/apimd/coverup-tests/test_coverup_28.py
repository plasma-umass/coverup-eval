# file apimd/parser.py:161-179
# lines [163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]
# branches ['163->164', '163->165', '166->167', '166->179', '167->168', '167->169', '170->171', '170->178', '171->172', '171->173', '174->175', '174->177']

import pytest
from apimd.parser import _e_type
from unittest.mock import Mock
from typing import Optional, Sequence
from ast import Constant

def test_e_type_empty_elements():
    assert _e_type() == ""

def test_e_type_none_element():
    assert _e_type(None) == ""

def test_e_type_non_constant_element():
    mock_expr = Mock()
    mock_expr.__iter__ = Mock(return_value=iter([Mock()]))
    assert _e_type(mock_expr) == ""

def test_e_type_mixed_constants():
    mock_expr1 = Mock()
    mock_expr1.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=1)]))
    mock_expr2 = Mock()
    mock_expr2.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value="string")]))
    assert _e_type(mock_expr1, mock_expr2) == "[int, str]"

def test_e_type_same_constants():
    mock_expr1 = Mock()
    mock_expr1.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=1)]))
    mock_expr2 = Mock()
    mock_expr2.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=2)]))
    assert _e_type(mock_expr1, mock_expr2) == "[int, int]"

def test_e_type_different_constants():
    mock_expr1 = Mock()
    mock_expr1.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=1)]))
    mock_expr2 = Mock()
    mock_expr2.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value="string")]))
    mock_expr3 = Mock()
    mock_expr3.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=3.14)]))
    assert _e_type(mock_expr1, mock_expr2, mock_expr3) == "[int, str, float]"

def test_e_type_mixed_types():
    mock_expr1 = Mock()
    mock_expr1.__iter__ = Mock(return_value=iter([Mock(spec=Constant, value=1), Mock(spec=Constant, value="string")]))
    assert _e_type(mock_expr1) == "[Any]"
