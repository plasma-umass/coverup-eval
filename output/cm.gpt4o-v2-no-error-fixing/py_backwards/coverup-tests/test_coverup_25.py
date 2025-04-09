# file: py_backwards/utils/snippet.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from typing import Dict
from typed_ast import ast3 as ast
from py_backwards.utils.snippet import VariablesReplacer, Variable

def test_variables_replacer_init():
    variables: Dict[str, Variable] = {"var1": "value1", "var2": "value2"}
    replacer = VariablesReplacer(variables)
    assert replacer._variables == variables
