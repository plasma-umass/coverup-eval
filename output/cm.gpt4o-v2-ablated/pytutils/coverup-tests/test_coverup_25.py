# file: pytutils/lazy/lazy_regex.py:202-206
# asked: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
import re
from unittest.mock import patch

# Assuming LazyRegex and _real_re_compile are defined somewhere in the module
from pytutils.lazy.lazy_regex import finditer_public, LazyRegex, _real_re_compile

class MockLazyRegex:
    def finditer(self, string):
        return re.finditer(r'\d+', string)

@pytest.fixture
def mock_lazy_regex(monkeypatch):
    monkeypatch.setattr('pytutils.lazy.lazy_regex.LazyRegex', MockLazyRegex)

@pytest.fixture
def mock_real_re_compile(monkeypatch):
    def mock_compile(pattern, flags=0):
        return re.compile(pattern, flags)
    monkeypatch.setattr('pytutils.lazy.lazy_regex._real_re_compile', mock_compile)

def test_finditer_public_with_lazy_regex(mock_lazy_regex):
    pattern = MockLazyRegex()
    string = "123 abc 456"
    result = list(finditer_public(pattern, string))
    assert len(result) == 2
    assert result[0].group() == '123'
    assert result[1].group() == '456'

def test_finditer_public_with_string_pattern(mock_real_re_compile):
    pattern = r'\d+'
    string = "123 abc 456"
    result = list(finditer_public(pattern, string))
    assert len(result) == 2
    assert result[0].group() == '123'
    assert result[1].group() == '456'
