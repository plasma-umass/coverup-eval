# file: apimd/parser.py:130-132
# asked: {"lines": [130, 132], "branches": []}
# gained: {"lines": [130, 132], "branches": []}

import pytest
from collections.abc import Iterable

# Assuming the _table_cell function is imported from apimd.parser
from apimd.parser import _table_cell

def test_table_cell():
    # Test with a list of strings
    items = ["cell1", "cell2", "cell3"]
    expected_output = "| cell1 | cell2 | cell3 |"
    assert _table_cell(items) == expected_output

    # Test with an empty list
    items = []
    expected_output = "||"
    assert _table_cell(items) == expected_output

    # Test with a single item
    items = ["single"]
    expected_output = "| single |"
    assert _table_cell(items) == expected_output

    # Test with multiple items containing spaces
    items = ["cell 1", "cell 2", "cell 3"]
    expected_output = "| cell 1 | cell 2 | cell 3 |"
    assert _table_cell(items) == expected_output

    # Test with non-string iterable
    items = [1, 2, 3]
    expected_output = "| 1 | 2 | 3 |"
    assert _table_cell(map(str, items)) == expected_output
