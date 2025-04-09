# file: pypara/dcc.py:355-360
# asked: {"lines": [355, 356, 360], "branches": []}
# gained: {"lines": [355, 356, 360], "branches": []}

import pytest
from unittest.mock import MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry():
    return DCCRegistryMachinery()

def test_table_property(dcc_registry):
    # Mocking DCC instances
    dcc1 = MagicMock(spec=DCC)
    dcc2 = MagicMock(spec=DCC)
    
    # Populating the buffers
    dcc_registry._buffer_main = {'DCC1': dcc1}
    dcc_registry._buffer_altn = {'DCC2': dcc2}
    
    # Accessing the table property
    table = dcc_registry.table
    
    # Assertions to verify the table content
    assert 'DCC1' in table
    assert 'DCC2' in table
    assert table['DCC1'] is dcc1
    assert table['DCC2'] is dcc2

    # Clean up
    dcc_registry._buffer_main.clear()
    dcc_registry._buffer_altn.clear()
