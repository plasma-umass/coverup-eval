# file py_backwards/transformers/base.py:127-136
# lines [127, 128, 129, 130, 132, 133, 134, 136]
# branches ['129->130', '129->132', '133->134', '133->136']

import ast
import pytest
from unittest.mock import MagicMock
from py_backwards.transformers.base import BaseImportRewrite

# Mocking the BaseImportRewrite class to test the visit_ImportFrom method
class MockBaseImportRewrite(BaseImportRewrite):
    def __init__(self):
        super().__init__(MagicMock())

    def _get_matched_rewrite(self, module):
        if module == 'module_to_rewrite':
            return 'new_module', None
        return None

    def _get_names_to_replace(self, node):
        if any(alias.name == 'name_to_replace' for alias in node.names):
            return [('name_to_replace', 'new_name')]
        return []

    def _replace_import_from_module(self, node, new_module, _):
        node.module = new_module
        return node

    def _replace_import_from_names(self, node, names_to_replace):
        new_names = []
        for alias in node.names:
            if alias.name in names_to_replace:
                new_names.append(ast.alias(name=names_to_replace[alias.name], asname=alias.asname))
            else:
                new_names.append(alias)
        node.names = new_names
        return node

# Test function to improve coverage
def test_visit_ImportFrom():
    transformer = MockBaseImportRewrite()

    # Test case for _get_matched_rewrite branch
    node_to_rewrite = ast.ImportFrom(module='module_to_rewrite', names=[ast.alias(name='name', asname=None)], level=0)
    rewritten_node = transformer.visit_ImportFrom(node_to_rewrite)
    assert rewritten_node.module == 'new_module'

    # Test case for _get_names_to_replace branch
    node_to_replace_name = ast.ImportFrom(module='module', names=[ast.alias(name='name_to_replace', asname=None)], level=0)
    replaced_name_node = transformer.visit_ImportFrom(node_to_replace_name)
    assert replaced_name_node.names[0].name == 'new_name'

    # Test case for no rewrite branch
    node_no_rewrite = ast.ImportFrom(module='module', names=[ast.alias(name='name', asname=None)], level=0)
    no_rewrite_node = transformer.visit_ImportFrom(node_no_rewrite)
    assert isinstance(no_rewrite_node, ast.ImportFrom)
    assert no_rewrite_node.module == 'module'
    assert no_rewrite_node.names[0].name == 'name'
