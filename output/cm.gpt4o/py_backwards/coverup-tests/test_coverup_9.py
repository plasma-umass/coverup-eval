# file py_backwards/utils/snippet.py:62-70
# lines [62, 63, 64, 65, 66, 68, 70]
# branches ['64->65', '64->68', '65->66', '65->68']

import ast
import pytest

from py_backwards.utils.snippet import VariablesReplacer

class MockVariablesReplacer(VariablesReplacer):
    def __init__(self):
        self._variables = {}

@pytest.fixture
def variables_replacer():
    replacer = MockVariablesReplacer()
    replacer._variables = {
        'old_module': 'new_module',
        'unchanged_module': 'unchanged_module',
        'partial.old_module': 'partial.new_module'
    }
    return replacer

def test_replace_module(variables_replacer):
    # Test case where the module name is fully replaced
    result = variables_replacer._replace_module('old_module')
    assert result == 'new_module'

    # Test case where the module name is not replaced
    result = variables_replacer._replace_module('unchanged_module')
    assert result == 'unchanged_module'

    # Test case where part of the module name is replaced
    result = variables_replacer._replace_module('partial.old_module')
    assert result == 'partial.new_module'

    # Test case where no part of the module name is replaced
    result = variables_replacer._replace_module('non_existent_module')
    assert result == 'non_existent_module'
