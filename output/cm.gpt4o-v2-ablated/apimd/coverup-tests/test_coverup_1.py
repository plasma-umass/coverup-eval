# file: apimd/parser.py:130-132
# asked: {"lines": [130, 132], "branches": []}
# gained: {"lines": [130, 132], "branches": []}

import pytest
from apimd.parser import _table_cell

def test_table_cell_single_item():
    result = _table_cell(["item1"])
    assert result == "| item1 |"

def test_table_cell_multiple_items():
    result = _table_cell(["item1", "item2", "item3"])
    assert result == "| item1 | item2 | item3 |"

def test_table_cell_empty():
    result = _table_cell([])
    assert result == "||"
