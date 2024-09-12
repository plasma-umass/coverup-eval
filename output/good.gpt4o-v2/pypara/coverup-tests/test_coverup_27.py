# file: pypara/dcc.py:355-360
# asked: {"lines": [355, 356, 360], "branches": []}
# gained: {"lines": [355, 356, 360], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from unittest.mock import MagicMock

def test_table_property():
    # Create a mock DCC object
    mock_dcc = MagicMock(spec=DCC)
    
    # Create an instance of DCCRegistryMachinery
    registry = DCCRegistryMachinery()
    
    # Populate the buffers with mock data
    registry._buffer_main = {'main_key': mock_dcc}
    registry._buffer_altn = {'altn_key': mock_dcc}
    
    # Access the table property
    table = registry.table
    
    # Assertions to verify the table content
    assert 'main_key' in table
    assert 'altn_key' in table
    assert table['main_key'] == mock_dcc
    assert table['altn_key'] == mock_dcc

    # Clean up
    registry._buffer_main.clear()
    registry._buffer_altn.clear()
