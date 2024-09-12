# file: apimd/parser.py:135-138
# asked: {"lines": [135, 137, 138], "branches": []}
# gained: {"lines": [135, 137, 138], "branches": []}

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with strings of length greater than 3
    result = _table_split(["hello", "world"])
    assert result == "|:-----:|:-----:|"

    # Test with strings of length less than or equal to 3
    result = _table_split(["hi", "bye"])
    assert result == "|:---:|:---:|"

    # Test with mixed length strings
    result = _table_split(["hi", "hello"])
    assert result == "|:---:|:-----:|"

    # Test with empty list
    result = _table_split([])
    assert result == "||"
