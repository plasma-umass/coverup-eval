# file py_backwards/transformers/base.py:87-94
# lines [87, 89, 90, 91, 92, 93, 94]
# branches ['89->exit', '89->90', '91->89', '91->92', '93->89', '93->94']

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite, BaseNodeTransformer

class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self):
        # Mock the BaseNodeTransformer's __init__ method
        pass

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        return MockBaseImportRewrite()

    def test_get_names_to_replace(self, transformer, mocker):
        # Mock the _get_matched_rewrite method to control its output
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new.module', 'new_name'))

        # Create a mock ImportFrom node
        node = ast.ImportFrom(
            module='old.module',
            names=[ast.alias(name='old_name', asname=None)],
            level=0
        )

        # Call the method and collect results
        result = list(transformer._get_names_to_replace(node))

        # Assertions to verify the correct behavior
        assert len(result) == 1
        assert result[0] == ('old.module.old_name', ('new.module', 'new_name'))

    def test_get_names_to_replace_no_rewrite(self, transformer, mocker):
        # Mock the _get_matched_rewrite method to return None
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=None)

        # Create a mock ImportFrom node
        node = ast.ImportFrom(
            module='old.module',
            names=[ast.alias(name='old_name', asname=None)],
            level=0
        )

        # Call the method and collect results
        result = list(transformer._get_names_to_replace(node))

        # Assertions to verify the correct behavior
        assert len(result) == 0

    def test_get_names_to_replace_wildcard(self, transformer, mocker):
        # Mock the _get_matched_rewrite method to control its output
        mocker.patch.object(transformer, '_get_matched_rewrite', return_value=('new.module', 'new_name'))

        # Create a mock ImportFrom node with a wildcard import
        node = ast.ImportFrom(
            module='old.module',
            names=[ast.alias(name='*', asname=None)],
            level=0
        )

        # Call the method and collect results
        result = list(transformer._get_names_to_replace(node))

        # Assertions to verify the correct behavior
        assert len(result) == 0
