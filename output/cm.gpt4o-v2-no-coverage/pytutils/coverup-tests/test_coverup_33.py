# file: pytutils/lazy/lazy_regex.py:202-206
# asked: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
import re
from pytutils.lazy.lazy_regex import finditer_public, LazyRegex

def test_finditer_public_with_lazyregex(mocker):
    pattern = LazyRegex(args=("test",))
    string = "this is a test string with test pattern"
    
    mock_match = mocker.Mock()
    mock_compile = mocker.patch.object(LazyRegex, 'finditer', return_value=iter([mock_match]))
    
    result = finditer_public(pattern, string)
    
    mock_compile.assert_called_once_with(string)
    assert list(result) == [mock_match]

def test_finditer_public_with_pattern(mocker):
    pattern = "test"
    string = "this is a test string with test pattern"
    
    mock_compile = mocker.patch('pytutils.lazy.lazy_regex._real_re_compile', return_value=re.compile(pattern))
    
    result = finditer_public(pattern, string)
    
    mock_compile.assert_called_once_with(pattern, 0)
    assert [match.group() for match in result] == [match.group() for match in re.finditer(pattern, string)]
