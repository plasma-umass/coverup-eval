# file: apimd/parser.py:130-132
# asked: {"lines": [130, 132], "branches": []}
# gained: {"lines": [130, 132], "branches": []}

import pytest
from collections.abc import Iterable
from apimd.parser import _table_cell

def test_table_cell_with_strings():
    items = ["item1", "item2", "item3"]
    expected_result = "| item1 | item2 | item3 |"
    assert _table_cell(items) == expected_result

def test_table_cell_with_empty_list():
    items = []
    expected_result = "||"
    assert _table_cell(items) == expected_result

def test_table_cell_with_single_item():
    items = ["item1"]
    expected_result = "| item1 |"
    assert _table_cell(items) == expected_result

def test_table_cell_with_non_string_items():
    items = [1, 2, 3]
    expected_result = "| 1 | 2 | 3 |"
    assert _table_cell(items) == expected_result
