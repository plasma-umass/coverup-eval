# file: pytutils/lazy/lazy_regex.py:202-206
# asked: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
import re
from pytutils.lazy.lazy_regex import finditer_public, LazyRegex

def test_finditer_public_with_lazyregex(mocker):
    # Create a mock LazyRegex object
    mock_lazy_regex = mocker.Mock(spec=LazyRegex)
    mock_finditer = mocker.Mock()
    mock_lazy_regex.finditer = mock_finditer

    # Call the function with the mock LazyRegex object
    result = finditer_public(mock_lazy_regex, "test string")

    # Assert that the finditer method of the LazyRegex object was called
    mock_finditer.assert_called_once_with("test string")
    # Assert that the result is the return value of the finditer method
    assert result == mock_finditer.return_value

def test_finditer_public_with_pattern(mocker):
    pattern = r"\d+"
    string = "There are 24 hours in a day and 60 minutes in an hour."

    # Mock the _real_re_compile function
    mock_compile = mocker.patch("pytutils.lazy.lazy_regex._real_re_compile", wraps=re.compile)

    # Call the function with a pattern string
    result = finditer_public(pattern, string)

    # Assert that _real_re_compile was called with the correct arguments
    mock_compile.assert_called_once_with(pattern, 0)
    # Assert that the result is an iterator
    assert hasattr(result, "__iter__")
    # Assert that the result contains the expected matches
    matches = [match.group() for match in result]
    assert matches == ["24", "60"]
