# file py_backwards/utils/snippet.py:42-44
# lines [42, 43, 44]
# branches []

import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

def test_variables_replacer_visit_functiondef():
    # Create a mock function definition node
    func_def_node = ast.FunctionDef(
        name='test_func',
        args=ast.arguments(
            posonlyargs=[],
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[],
        decorator_list=[]
    )

    # Create an instance of VariablesReplacer with a mock variables dictionary
    replacer = VariablesReplacer(variables={'test_func': 'new_test_func'})

    # Visit the function definition node
    new_node = replacer.visit_FunctionDef(func_def_node)

    # Assert that the node is still a FunctionDef
    assert isinstance(new_node, ast.FunctionDef)

    # Assert that the name field has been replaced
    assert new_node.name == 'new_test_func'

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code if necessary
    yield
    # Add any necessary cleanup code here
