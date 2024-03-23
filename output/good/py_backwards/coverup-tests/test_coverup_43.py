# file py_backwards/transformers/base.py:43-52
# lines [45, 46, 48, 49, 50, 52]
# branches ['45->46', '45->48', '48->49', '48->52', '49->48', '49->50']

import pytest
from unittest.mock import MagicMock
from py_backwards.transformers.base import BaseImportRewrite
from typing import Optional, Tuple

class TestBaseImportRewrite(BaseImportRewrite):
    rewrites = [('old_module', 'new_module')]

def test_get_matched_rewrite(mocker):
    mocker.patch('py_backwards.transformers.base.BaseNodeTransformer.__init__', return_value=None)
    transformer = TestBaseImportRewrite(tree=MagicMock())

    # Test the case where name is None
    assert transformer._get_matched_rewrite(None) is None

    # Test the case where name matches exactly
    assert transformer._get_matched_rewrite('old_module') == ('old_module', 'new_module')

    # Test the case where name starts with the matched name followed by a dot
    assert transformer._get_matched_rewrite('old_module.submodule') == ('old_module', 'new_module')

    # Test the case where name does not match
    assert transformer._get_matched_rewrite('unmatched_module') is None
