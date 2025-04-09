# file: py_backwards/utils/snippet.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer, Variable

class MockVariable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_variables_replacer_init():
    variables = {'var1': MockVariable(name='var1', value=1)}
    replacer = VariablesReplacer(variables)
    assert replacer._variables == variables
