# file: apimd/parser.py:135-138
# asked: {"lines": [135, 137, 138], "branches": []}
# gained: {"lines": [135, 137, 138], "branches": []}

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with strings of varying lengths
    result = _table_split(["a", "ab", "abc", "abcd"])
    assert result == "|:---:|:---:|:---:|:----:|"

    # Test with empty string
    result = _table_split([""])
    assert result == "|:---:|"

    # Test with all strings of length greater than 3
    result = _table_split(["abcd", "efgh", "ijkl"])
    assert result == "|:----:|:----:|:----:|"

    # Test with all strings of length 3 or less
    result = _table_split(["a", "ab", "abc"])
    assert result == "|:---:|:---:|:---:|"

    # Test with mixed empty and non-empty strings
    result = _table_split(["", "a", "abcd"])
    assert result == "|:---:|:---:|:----:|"
