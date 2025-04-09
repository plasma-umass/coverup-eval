# file apimd/parser.py:135-138
# lines [135, 137, 138]
# branches []

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with a variety of input lengths
    args = ["a", "ab", "abc", "abcd"]
    result = _table_split(args)
    expected = "|:---:|:---:|:---:|:----:|"
    assert result == expected

    # Test with empty input
    args = []
    result = _table_split(args)
    expected = "||"
    assert result == expected

    # Test with single short input
    args = ["a"]
    result = _table_split(args)
    expected = "|:---:|"
    assert result == expected

    # Test with single long input
    args = ["abcd"]
    result = _table_split(args)
    expected = "|:----:|"
    assert result == expected

    # Test with mixed length inputs
    args = ["a", "abcd"]
    result = _table_split(args)
    expected = "|:---:|:----:|"
    assert result == expected
