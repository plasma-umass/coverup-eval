# file apimd/parser.py:130-132
# lines [130, 132]
# branches []

import pytest
from apimd.parser import _table_cell

def test_table_cell():
    # Test with a single item
    single_item = ["Item1"]
    expected_single = "| Item1 |"
    assert _table_cell(single_item) == expected_single

    # Test with multiple items
    multiple_items = ["Item1", "Item2", "Item3"]
    expected_multiple = "| Item1 | Item2 | Item3 |"
    assert _table_cell(multiple_items) == expected_multiple

    # Test with no items
    no_items = []
    expected_no_items = "||"
    assert _table_cell(no_items) == expected_no_items

    # Test with items containing special characters
    special_items = ["Item|1", "It<em>2", "It**3**"]
    expected_special = "| Item|1 | It<em>2 | It**3** |"
    assert _table_cell(special_items) == expected_special

    # Test with items that are numbers (non-string)
    number_items = [1, 2, 3]
    expected_number = "| 1 | 2 | 3 |"
    assert _table_cell(map(str, number_items)) == expected_number
