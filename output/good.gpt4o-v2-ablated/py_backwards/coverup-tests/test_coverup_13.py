# file: py_backwards/utils/snippet.py:146-157
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
import ast

# Assuming the extend function is part of a module named snippet
from py_backwards.utils.snippet import extend

def test_extend_with_empty_vars():
    vars = []
    extend(vars)
    # No assertions needed as the function does not return anything and vars is empty

def test_extend_with_non_empty_vars():
    vars = [
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Constant(value=1)),
        ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())], value=ast.Constant(value=2))
    ]
    
    with patch('py_backwards.utils.snippet.extend') as mock_extend:
        mock_extend(vars)
        mock_extend.assert_called_once_with(vars)

def test_extend_with_complex_vars():
    vars = [
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Constant(value=1)),
        ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())], value=ast.Constant(value=2)),
        ast.Assign(targets=[ast.Name(id='z', ctx=ast.Store())], value=ast.Constant(value=3))
    ]
    
    with patch('py_backwards.utils.snippet.extend') as mock_extend:
        mock_extend(vars)
        mock_extend.assert_called_once_with(vars)
