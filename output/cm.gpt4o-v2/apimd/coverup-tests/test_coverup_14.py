# file: apimd/parser.py:130-132
# asked: {"lines": [130, 132], "branches": []}
# gained: {"lines": [130, 132], "branches": []}

import pytest
from collections.abc import Iterable
from apimd.parser import _table_cell

def test_table_cell():
    items = ["item1", "item2", "item3"]
    expected_output = "| item1 | item2 | item3 |"
    assert _table_cell(items) == expected_output

    # Test with empty list
    items = []
    expected_output = "||"
    assert _table_cell(items) == expected_output

    # Test with single item
    items = ["item1"]
    expected_output = "| item1 |"
    assert _table_cell(items) == expected_output

    # Test with special characters
    items = ["item1", "item|2", "item3"]
    expected_output = "| item1 | item|2 | item3 |"
    assert _table_cell(items) == expected_output

    # Test with numbers
    items = ["1", "2", "3"]
    expected_output = "| 1 | 2 | 3 |"
    assert _table_cell(items) == expected_output

    # Test with mixed types
    items = ["item1", "2", "item3"]
    expected_output = "| item1 | 2 | item3 |"
    assert _table_cell(items) == expected_output
