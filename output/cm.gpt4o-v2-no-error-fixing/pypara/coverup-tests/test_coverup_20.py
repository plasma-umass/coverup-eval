# file: pypara/dcc.py:355-360
# asked: {"lines": [355, 356, 360], "branches": []}
# gained: {"lines": [355, 356, 360], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from decimal import Decimal
from unittest.mock import MagicMock

def test_table_property():
    # Create a mock DCC object
    mock_dcc_main = MagicMock(spec=DCC)
    mock_dcc_altn = MagicMock(spec=DCC)

    # Create an instance of DCCRegistryMachinery
    registry = DCCRegistryMachinery()

    # Populate the _buffer_main and _buffer_altn with mock DCC objects
    registry._buffer_main = {'main_dcc': mock_dcc_main}
    registry._buffer_altn = {'altn_dcc': mock_dcc_altn}

    # Access the table property
    table = registry.table

    # Assertions to verify the table property returns the correct combined dictionary
    assert 'main_dcc' in table
    assert 'altn_dcc' in table
    assert table['main_dcc'] is mock_dcc_main
    assert table['altn_dcc'] is mock_dcc_altn

    # Clean up
    registry._buffer_main.clear()
    registry._buffer_altn.clear()
