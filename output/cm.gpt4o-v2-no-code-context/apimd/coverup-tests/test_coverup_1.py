# file: apimd/parser.py:130-132
# asked: {"lines": [130, 132], "branches": []}
# gained: {"lines": [130, 132], "branches": []}

import pytest
from apimd.parser import _table_cell

def test_table_cell_with_items():
    items = ["item1", "item2", "item3"]
    expected_output = "| item1 | item2 | item3 |"
    assert _table_cell(items) == expected_output

def test_table_cell_with_empty_items():
    items = []
    expected_output = "||"
    assert _table_cell(items) == expected_output
