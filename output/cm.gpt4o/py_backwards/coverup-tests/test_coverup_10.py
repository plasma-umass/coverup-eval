# file py_backwards/utils/snippet.py:28-36
# lines [28, 29, 30, 31, 32, 33, 34, 36]
# branches ['30->31', '30->36', '31->32', '31->33', '33->34', '33->36']

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_variables_replacer_replace_field_or_node():
    class TestNode:
        def __init__(self, value):
            self.value = value

    class TestVariablesReplacer(VariablesReplacer):
        def __init__(self):
            self._variables = {}

    replacer = TestVariablesReplacer()
    replacer._variables = {
        'old_value': 'new_value',
        'node_value': TestNode('replaced_node')
    }

    # Test case where value is replaced with a string
    node = TestNode('old_value')
    result = replacer._replace_field_or_node(node, 'value')
    assert result.value == 'new_value'

    # Test case where node is replaced with another node
    node = TestNode('node_value')
    result = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert isinstance(result, TestNode)
    assert result.value == 'replaced_node'

    # Test case where node is replaced with another node of the same type
    node = TestNode('node_value')
    result = replacer._replace_field_or_node(node, 'value')
    assert isinstance(result, TestNode)
    assert result.value == 'replaced_node'
