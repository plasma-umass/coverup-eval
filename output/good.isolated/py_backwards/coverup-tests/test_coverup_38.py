# file py_backwards/utils/snippet.py:50-52
# lines [51, 52]
# branches []

import ast
from py_backwards.utils.snippet import VariablesReplacer
import pytest

def test_variables_replacer_visits_keyword_node():
    # Create a keyword node with a string value that should not be replaced
    keyword_node = ast.keyword(arg='test_arg', value=ast.Str(s='test_value'))

    # Create an instance of VariablesReplacer with an empty dictionary for variables
    replacer = VariablesReplacer(variables={})

    # Visit the keyword node
    new_keyword_node = replacer.visit_keyword(keyword_node)

    # Assert that the keyword node is returned unchanged
    assert new_keyword_node.arg == 'test_arg'
    assert isinstance(new_keyword_node.value, ast.Str)
    assert new_keyword_node.value.s == 'test_value'

    # Assert that the node is an instance of ast.keyword
    assert isinstance(new_keyword_node, ast.keyword)
