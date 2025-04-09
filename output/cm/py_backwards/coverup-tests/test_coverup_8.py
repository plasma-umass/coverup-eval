# file py_backwards/transformers/base.py:68-73
# lines [68, 69, 70, 71, 73]
# branches ['70->71', '70->73']

import ast
from py_backwards.transformers.base import BaseImportRewrite
import pytest

# Mocking the BaseImportRewrite to test the visit_Import method
class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self, tree):
        super().__init__(tree)

    def _get_matched_rewrite(self, name):
        if name == 'mocked_module':
            return ('new_module', 'new_name')
        return None

    def _replace_import(self, node, new_module, new_name):
        return ast.Import(names=[ast.alias(name=new_name, asname=None)])

# Test function to cover the missing branches
def test_visit_import(mocker):
    mocker.patch.object(MockBaseImportRewrite, '_get_matched_rewrite')
    mocker.patch.object(MockBaseImportRewrite, '_replace_import')

    transformer = MockBaseImportRewrite(tree=ast.AST())

    # Test with a module that should be rewritten
    mock_import = ast.Import(names=[ast.alias(name='mocked_module', asname=None)])
    transformer._get_matched_rewrite.return_value = ('new_module', 'new_name')
    transformer._replace_import.return_value = ast.Import(names=[ast.alias(name='new_name', asname=None)])
    new_node = transformer.visit_Import(mock_import)
    assert isinstance(new_node, ast.Import)
    assert new_node.names[0].name == 'new_name'

    # Test with a module that should not be rewritten
    mock_import = ast.Import(names=[ast.alias(name='other_module', asname=None)])
    transformer._get_matched_rewrite.return_value = None
    new_node = transformer.visit_Import(mock_import)
    assert isinstance(new_node, ast.Import)
    assert new_node.names[0].name == 'other_module'
