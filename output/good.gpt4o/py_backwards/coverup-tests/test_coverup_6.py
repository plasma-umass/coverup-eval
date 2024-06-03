# file py_backwards/transformers/base.py:43-52
# lines [43, 45, 46, 48, 49, 50, 52]
# branches ['45->46', '45->48', '48->49', '48->52', '49->48', '49->50']

import pytest
from py_backwards.transformers.base import BaseImportRewrite
from unittest.mock import MagicMock

class TestBaseImportRewrite:
    @pytest.fixture
    def transformer(self):
        class TestTransformer(BaseImportRewrite):
            rewrites = [
                ('old_module', 'new_module'),
                ('another_old', 'another_new')
            ]
        return TestTransformer(tree=MagicMock())

    def test_get_matched_rewrite_none(self, transformer):
        assert transformer._get_matched_rewrite(None) is None

    def test_get_matched_rewrite_exact_match(self, transformer):
        assert transformer._get_matched_rewrite('old_module') == ('old_module', 'new_module')

    def test_get_matched_rewrite_prefix_match(self, transformer):
        assert transformer._get_matched_rewrite('old_module.submodule') == ('old_module', 'new_module')

    def test_get_matched_rewrite_no_match(self, transformer):
        assert transformer._get_matched_rewrite('non_existent_module') is None
