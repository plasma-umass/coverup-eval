# file: py_backwards/utils/snippet.py:62-70
# asked: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66], [65, 68]]}
# gained: {"lines": [62, 63, 64, 65, 66, 68, 70], "branches": [[64, 65], [64, 68], [65, 66]]}

import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    @pytest.fixture
    def replacer(self):
        class MockVariablesReplacer(VariablesReplacer):
            def __init__(self, variables):
                self._variables = variables

        return MockVariablesReplacer

    def test_replace_module_with_replacement(self, replacer):
        variables = {'a': 'x', 'b': 'y'}
        instance = replacer(variables)
        result = instance._replace_module('a.b.c')
        assert result == 'x.y.c'

    def test_replace_module_without_replacement(self, replacer):
        variables = {'a': 'x'}
        instance = replacer(variables)
        result = instance._replace_module('a.b.c')
        assert result == 'x.b.c'

    def test_replace_module_no_variables(self, replacer):
        variables = {}
        instance = replacer(variables)
        result = instance._replace_module('a.b.c')
        assert result == 'a.b.c'
