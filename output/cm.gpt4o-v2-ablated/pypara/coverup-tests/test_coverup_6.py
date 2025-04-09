# file: pypara/dcc.py:294-302
# asked: {"lines": [294, 299, 302], "branches": []}
# gained: {"lines": [294, 299, 302], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery

def test_dcc_registry_machinery_initialization():
    registry = DCCRegistryMachinery()
    
    # Verify that the main buffer is initialized correctly
    assert registry._buffer_main == {}
    
    # Verify that the alternative buffer is initialized correctly
    assert registry._buffer_altn == {}
