# file: pytutils/lazy/lazy_regex.py:202-206
# asked: {"lines": [202, 203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [202, 203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
from pytutils.lazy.lazy_regex import LazyRegex, finditer_public

class MockLazyRegex:
    def __init__(self, pattern):
        self.pattern = pattern

    def finditer(self, string):
        return iter([self.pattern])

@pytest.fixture
def mock_lazy_regex(monkeypatch):
    monkeypatch.setattr('pytutils.lazy.lazy_regex.LazyRegex', MockLazyRegex)

def test_finditer_public_with_lazyregex(mock_lazy_regex):
    pattern = MockLazyRegex('test')
    result = finditer_public(pattern, 'test string')
    assert list(result) == ['test']

def test_finditer_public_with_string_pattern():
    pattern = 'test'
    result = finditer_public(pattern, 'test string')
    assert list(result) != []
