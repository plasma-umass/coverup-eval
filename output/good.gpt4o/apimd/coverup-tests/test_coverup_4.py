# file apimd/parser.py:130-132
# lines [130, 132]
# branches []

import pytest
from apimd.parser import _table_cell

def test_table_cell():
    # Test with multiple items
    items = ["cell1", "cell2", "cell3"]
    result = _table_cell(items)
    assert result == "| cell1 | cell2 | cell3 |"

    # Test with a single item
    items = ["single"]
    result = _table_cell(items)
    assert result == "| single |"

    # Test with no items
    items = []
    result = _table_cell(items)
    assert result == "||"

    # Test with items containing special characters
    items = ["cell|1", "cell|2"]
    result = _table_cell(items)
    assert result == "| cell|1 | cell|2 |"

    # Test with items containing spaces
    items = ["cell 1", "cell 2"]
    result = _table_cell(items)
    assert result == "| cell 1 | cell 2 |"
