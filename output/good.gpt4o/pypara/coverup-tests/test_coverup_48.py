# file pypara/dcc.py:355-360
# lines [355, 356, 360]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the DCC class and DCCRegistryMachinery class are defined in pypara.dcc
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def mock_dcc_registry_machinery(mocker):
    # Create a mock instance of DCCRegistryMachinery
    mock_instance = DCCRegistryMachinery()
    # Create mock DCC instances with required arguments
    mock_dcc1 = DCC('name1', 'altnames1', 'currencies1', 'calculate_fraction_method1')
    mock_dcc2 = DCC('name2', 'altnames2', 'currencies2', 'calculate_fraction_method2')
    mock_dcc3 = DCC('name3', 'altnames3', 'currencies3', 'calculate_fraction_method3')
    mock_dcc4 = DCC('name4', 'altnames4', 'currencies4', 'calculate_fraction_method4')
    mock_instance._buffer_main = {'main_key1': mock_dcc1, 'main_key2': mock_dcc2}
    mock_instance._buffer_altn = {'altn_key1': mock_dcc3, 'altn_key2': mock_dcc4}
    return mock_instance

def test_table_property(mock_dcc_registry_machinery):
    # Access the table property
    table = mock_dcc_registry_machinery.table

    # Verify the table contains the expected keys and values
    assert 'main_key1' in table
    assert 'main_key2' in table
    assert 'altn_key1' in table
    assert 'altn_key2' in table

    # Verify the values are instances of DCC
    assert isinstance(table['main_key1'], DCC)
    assert isinstance(table['main_key2'], DCC)
    assert isinstance(table['altn_key1'], DCC)
    assert isinstance(table['altn_key2'], DCC)
