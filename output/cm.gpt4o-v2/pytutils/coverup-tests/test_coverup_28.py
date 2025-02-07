# file: pytutils/lazy/lazy_regex.py:202-206
# asked: {"lines": [202, 203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [202, 203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
import re
from pytutils.lazy.lazy_regex import finditer_public, LazyRegex

def test_finditer_public_with_lazyregex(mocker):
    # Mock the LazyRegex object and its finditer method
    mock_lazyregex = mocker.Mock(spec=LazyRegex)
    mock_finditer = mocker.Mock()
    mock_lazyregex.finditer = mock_finditer

    # Call the function with the mocked LazyRegex object
    result = finditer_public(mock_lazyregex, "test string")

    # Assert that the finditer method was called on the LazyRegex object
    mock_finditer.assert_called_once_with("test string")
    assert result == mock_finditer()

def test_finditer_public_with_pattern(mocker):
    # Mock the _real_re_compile function
    mock_compile = mocker.patch('pytutils.lazy.lazy_regex._real_re_compile', side_effect=re.compile)

    # Call the function with a pattern string
    pattern = r"\d+"
    result = finditer_public(pattern, "test string 123")

    # Assert that _real_re_compile was called with the correct arguments
    mock_compile.assert_called_once_with(pattern, 0)

    # Assert that the result is an iterator
    assert hasattr(result, '__iter__')

    # Assert that the iterator yields the expected matches
    matches = list(result)
    assert len(matches) == 1
    assert matches[0].group() == "123"
