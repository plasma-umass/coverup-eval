# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_replace_module_with_replacement():
    variables = {'a': 'x', 'b': 'y'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('a.b.c')
    assert result == 'x.y.c'

def test_replace_module_without_replacement():
    variables = {'a': 'x', 'b': 'y'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('d.e.f')
    assert result == 'd.e.f'

def test_replace_module_partial_replacement():
    variables = {'a': 'x', 'b': 'y'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('a.e.f')
    assert result == 'x.e.f'
