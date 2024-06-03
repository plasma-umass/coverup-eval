# file pytutils/lazy/lazy_regex.py:202-206
# lines [203, 204, 206]
# branches ['203->204', '203->206']

import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex, finditer_public

class MockLazyRegex:
    def __init__(self, pattern):
        self.pattern = pattern

    def finditer(self, string):
        return [(m.start(), m.end()) for m in re.finditer(self.pattern, string)]

def test_finditer_public_with_lazy_regex(mocker):
    mock_pattern = MockLazyRegex(r'\d+')
    mocker.patch('pytutils.lazy.lazy_regex.LazyRegex', MockLazyRegex)
    result = finditer_public(mock_pattern, '123 abc 456')
    assert list(result) == [(0, 3), (8, 11)]

def test_finditer_public_with_regular_pattern():
    result = finditer_public(r'\d+', '123 abc 456')
    assert [match.span() for match in result] == [(0, 3), (8, 11)]
