# file: apimd/parser.py:135-138
# asked: {"lines": [135, 137, 138], "branches": []}
# gained: {"lines": [135, 137, 138], "branches": []}

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with strings longer than 3 characters
    result = _table_split(["hello", "world"])
    assert result == '|:-----:|:-----:|'

    # Test with strings of length 3
    result = _table_split(["abc", "def"])
    assert result == '|:---:|:---:|'

    # Test with strings shorter than 3 characters
    result = _table_split(["a", "bc"])
    assert result == '|:---:|:---:|'

    # Test with an empty list
    result = _table_split([])
    assert result == '||'

    # Test with mixed length strings
    result = _table_split(["a", "abcd", "ef"])
    assert result == '|:---:|:----:|:---:|'
