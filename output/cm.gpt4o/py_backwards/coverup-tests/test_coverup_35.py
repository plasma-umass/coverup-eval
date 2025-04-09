# file py_backwards/utils/snippet.py:25-26
# lines [25, 26]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_variables_replacer_init():
    variables = {"var1": Variable(name="var1", value=1), "var2": Variable(name="var2", value=2)}
    replacer = VariablesReplacer(variables)
    
    assert replacer._variables == variables
