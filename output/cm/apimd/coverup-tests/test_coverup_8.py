# file apimd/parser.py:135-138
# lines [135, 137, 138]
# branches []

import pytest
from apimd.parser import _table_split

def test_table_split():
    # Test with varying lengths of arguments
    args_short = ["a", "bb", "ccc"]
    args_long = ["longer", "entries", "here"]
    
    expected_short = "|:---:|:---:|:---:|"
    expected_long = "|:------:|:-------:|:----:|"
    
    assert _table_split(args_short) == expected_short, "Table split for short args did not match expected format"
    assert _table_split(args_long) == expected_long, "Table split for long args did not match expected format"
