# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [], "branches": [[65, 68]]}
# gained: {"lines": [], "branches": [[65, 68]]}

import pytest
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer

def test_replace_module_with_string_variable():
    variables = {'os': 'operating_system'}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('os.path')
    assert result == 'operating_system.path'

def test_replace_module_with_non_string_variable():
    variables = {'os': 123}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('os.path')
    assert result == 'os.path'

def test_replace_module_with_no_variable():
    variables = {}
    replacer = VariablesReplacer(variables)
    result = replacer._replace_module('os.path')
    assert result == 'os.path'
