# file: py_backwards/transformers/base.py:43-52
# asked: {"lines": [43, 45, 46, 48, 49, 50, 52], "branches": [[45, 46], [45, 48], [48, 49], [48, 52], [49, 48], [49, 50]]}
# gained: {"lines": [43, 45, 46, 48, 49, 50, 52], "branches": [[45, 46], [45, 48], [48, 49], [48, 52], [49, 48], [49, 50]]}

import pytest
from py_backwards.transformers.base import BaseImportRewrite
from typed_ast import ast3 as ast

@pytest.fixture
def transformer():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('moduleA', 'moduleB'),
            ('moduleC.sub', 'moduleD.sub'),
        ]
    return TestTransformer(None)

def test_get_matched_rewrite_none(transformer):
    assert transformer._get_matched_rewrite(None) is None

def test_get_matched_rewrite_exact_match(transformer):
    assert transformer._get_matched_rewrite('moduleA') == ('moduleA', 'moduleB')

def test_get_matched_rewrite_prefix_match(transformer):
    assert transformer._get_matched_rewrite('moduleC.sub.module') == ('moduleC.sub', 'moduleD.sub')

def test_get_matched_rewrite_no_match(transformer):
    assert transformer._get_matched_rewrite('moduleX') is None
