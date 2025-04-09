# file py_backwards/utils/snippet.py:62-70
# lines []
# branches ['65->68']

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_replace_module_with_non_str_variable():
    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self):
            self._variables = {'some_module': 123}

    replacer = TestVariablesReplacer()

    module_name = 'some_module.sub_module'
    result = replacer._replace_module(module_name)

    assert result == 'some_module.sub_module'
