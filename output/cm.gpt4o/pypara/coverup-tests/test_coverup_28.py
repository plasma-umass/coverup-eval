# file pypara/dcc.py:294-302
# lines [294, 299, 302]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

def test_dcc_registry_machinery_initialization():
    # Create an instance of DCCRegistryMachinery
    registry = DCCRegistryMachinery()
    
    # Assert that the main buffer is initialized as an empty dictionary
    assert registry._buffer_main == {}
    
    # Assert that the alternative buffer is initialized as an empty dictionary
    assert registry._buffer_altn == {}
