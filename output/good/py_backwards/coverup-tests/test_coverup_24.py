# file py_backwards/transformers/base.py:40-42
# lines [40, 41]
# branches []

import pytest
from py_backwards.transformers.base import BaseNodeTransformer
from unittest.mock import MagicMock

class TestBaseImportRewrite(BaseNodeTransformer):
    rewrites = [('old_module', 'new_module')]

def test_base_import_rewrite():
    tree = MagicMock()
    transformer = TestBaseImportRewrite(tree)
    assert transformer.rewrites == [('old_module', 'new_module')]
