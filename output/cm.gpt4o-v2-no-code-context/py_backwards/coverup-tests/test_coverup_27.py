# file: py_backwards/utils/snippet.py:85-90
# asked: {"lines": [85, 86, 88, 89, 90], "branches": []}
# gained: {"lines": [85, 86, 88, 89, 90], "branches": []}

import ast
import pytest
from typing import Dict
from py_backwards.utils.snippet import VariablesReplacer

class TestVariablesReplacer:
    def test_replace_method(self, mocker):
        # Mock the visit method to ensure it gets called
        mock_visit = mocker.patch.object(VariablesReplacer, 'visit', return_value=None)

        # Create a simple AST tree
        tree = ast.parse("x = 1")

        # Define variables to replace
        variables = {"x": "y"}

        # Call the replace method
        replaced_tree = VariablesReplacer.replace(tree, variables)

        # Verify that the tree was visited
        mock_visit.assert_called_once_with(tree)

        # Verify that the tree returned is the same as the input tree
        assert replaced_tree is tree
