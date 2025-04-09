# file: pypara/dcc.py:294-302
# asked: {"lines": [294, 299, 302], "branches": []}
# gained: {"lines": [294, 299, 302], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery

def test_dcc_registry_machinery_initialization():
    registry = DCCRegistryMachinery()
    
    # Assert that the main buffer is initialized correctly
    assert isinstance(registry._buffer_main, dict)
    assert len(registry._buffer_main) == 0
    
    # Assert that the alternative names buffer is initialized correctly
    assert isinstance(registry._buffer_altn, dict)
    assert len(registry._buffer_altn) == 0
