# file pypara/dcc.py:348-353
# lines [348, 349, 353]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the DCC class and DCCRegistryMachinery class are defined in pypara.dcc
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def mock_dcc_registry_machinery():
    # Create a mock instance of DCCRegistryMachinery
    mock_instance = DCCRegistryMachinery()
    # Mock the _buffer_main attribute
    mock_instance._buffer_main = {
        'key1': MagicMock(spec=DCC),
        'key2': MagicMock(spec=DCC)
    }
    return mock_instance

def test_registry_property(mock_dcc_registry_machinery):
    # Access the registry property
    registry = mock_dcc_registry_machinery.registry
    
    # Assert that the registry contains the expected number of items
    assert len(registry) == 2
    
    # Assert that the items in the registry are instances of DCC
    for item in registry:
        assert isinstance(item, DCC)
