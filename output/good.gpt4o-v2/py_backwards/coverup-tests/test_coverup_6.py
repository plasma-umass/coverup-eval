# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66]]}

import pytest
from py_backwards.utils.snippet import VariablesReplacer
from typed_ast import ast3 as ast

def test_replace_module_with_replacement():
    variables = {'a': 'b'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('a.c')
    assert result == 'b.c'

def test_replace_module_without_replacement():
    variables = {'a': 'b'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('x.y')
    assert result == 'x.y'

def test_replace_module_partial_replacement():
    variables = {'a': 'b', 'x': 'y'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('a.x')
    assert result == 'b.y'
