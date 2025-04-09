# file: py_backwards/transformers/dict_unpacking.py:67-69
# asked: {"lines": [67, 68, 69], "branches": []}
# gained: {"lines": [67, 68, 69], "branches": []}

import ast
import pytest
from unittest.mock import patch, MagicMock
from py_backwards.transformers.dict_unpacking import DictUnpackingTransformer

class TestDictUnpackingTransformer:
    @patch('py_backwards.transformers.dict_unpacking.insert_at')
    @patch('py_backwards.transformers.dict_unpacking.merge_dicts.get_body', return_value=ast.Pass())
    def test_visit_module(self, mock_merge_dicts_get_body, mock_insert_at):
        # Create a sample AST node
        node = ast.Module(body=[])

        # Create a mock tree to pass to the transformer
        mock_tree = MagicMock()

        # Instantiate the transformer and call visit_Module
        transformer = DictUnpackingTransformer(mock_tree)
        result = transformer.visit_Module(node)

        # Assertions to verify the behavior
        mock_insert_at.assert_called_once_with(0, node, mock_merge_dicts_get_body.return_value)
        assert result is node
