# file py_backwards/utils/snippet.py:25-26
# lines [25, 26]
# branches []

import pytest
from py_backwards.utils.snippet import VariablesReplacer
import ast

# Test function to cover the __init__ method of VariablesReplacer
def test_variables_replacer_init():
    variables = {'x': 'VariableX', 'y': 'VariableY'}
    replacer = VariablesReplacer(variables)
    assert replacer._variables == variables
