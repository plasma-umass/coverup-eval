# file py_backwards/utils/snippet.py:54-56
# lines [54, 55, 56]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_visit_ClassDef(mocker):
    # Create a mock for the _replace_field_or_node method
    mocker.patch.object(VariablesReplacer, '_replace_field_or_node', return_value=ast.ClassDef(name='ReplacedClass', bases=[], keywords=[], body=[], decorator_list=[]))

    # Create an instance of VariablesReplacer with a dummy 'variables' argument
    replacer = VariablesReplacer(variables={})

    # Create a sample ClassDef node
    class_node = ast.ClassDef(name='OriginalClass', bases=[], keywords=[], body=[], decorator_list=[])

    # Visit the ClassDef node
    result_node = replacer.visit_ClassDef(class_node)

    # Assert that the _replace_field_or_node method was called with the correct arguments
    VariablesReplacer._replace_field_or_node.assert_called_once_with(class_node, 'name')

    # Assert that the name of the class was replaced
    assert result_node.name == 'ReplacedClass'

    # Assert that the result node is still a ClassDef
    assert isinstance(result_node, ast.ClassDef)
