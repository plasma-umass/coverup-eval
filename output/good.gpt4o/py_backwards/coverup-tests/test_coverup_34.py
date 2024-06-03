# file py_backwards/transformers/base.py:40-42
# lines [40, 41]
# branches []

import pytest
from py_backwards.transformers.base import BaseImportRewrite
from unittest.mock import Mock

def test_base_import_rewrite():
    # Mock the required 'tree' argument for the BaseNodeTransformer
    mock_tree = Mock()

    # Create an instance of the BaseImportRewrite class with the mock tree
    transformer = BaseImportRewrite(mock_tree)
    
    # Check that the rewrites attribute is an empty list
    assert transformer.rewrites == []

    # Modify the rewrites attribute and check the change
    transformer.rewrites.append(('old_module', 'new_module'))
    assert transformer.rewrites == [('old_module', 'new_module')]

    # Clean up by resetting the rewrites attribute to an empty list
    transformer.rewrites = []
    assert transformer.rewrites == []
