# file: apimd/parser.py:135-138
# asked: {"lines": [135, 137, 138], "branches": []}
# gained: {"lines": [135, 137, 138], "branches": []}

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with an empty list
    result = _table_split([])
    assert result == '||'

    # Test with a list of strings of varying lengths
    result = _table_split(['a', 'ab', 'abc', 'abcd'])
    assert result == '|:---:|:---:|:---:|:----:|'

    # Test with a list of strings all shorter than 3 characters
    result = _table_split(['a', 'b', 'c'])
    assert result == '|:---:|:---:|:---:|'

    # Test with a list of strings all longer than 3 characters
    result = _table_split(['abcd', 'efgh', 'ijkl'])
    assert result == '|:----:|:----:|:----:|'
