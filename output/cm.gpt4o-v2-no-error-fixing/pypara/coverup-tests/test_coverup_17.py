# file: pypara/dcc.py:348-353
# asked: {"lines": [348, 349, 353], "branches": []}
# gained: {"lines": [348, 349, 353], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from unittest.mock import MagicMock

def test_registry_property():
    # Create a mock DCC object
    mock_dcc = MagicMock(spec=DCC)
    
    # Create an instance of DCCRegistryMachinery
    registry_machinery = DCCRegistryMachinery()
    
    # Add the mock DCC object to the _buffer_main dictionary
    registry_machinery._buffer_main['mock_dcc'] = mock_dcc
    
    # Access the registry property
    registry = registry_machinery.registry
    
    # Assert that the registry contains the mock DCC object
    assert registry == [mock_dcc]
    
    # Clean up
    del registry_machinery._buffer_main['mock_dcc']
