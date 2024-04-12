# file pypara/dcc.py:304-308
# lines [304, 308]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def dcc_registry_machinery():
    class DCCRegistryMachineryTest(DCCRegistryMachinery):
        def __init__(self):
            self._buffer_main = set()
            self._buffer_altn = set()
    return DCCRegistryMachineryTest()

def test_is_registered(dcc_registry_machinery):
    # Test when name is not registered
    assert not dcc_registry_machinery._is_registered("test_name")
    
    # Register name in _buffer_main and test
    dcc_registry_machinery._buffer_main.add("test_name")
    assert dcc_registry_machinery._is_registered("test_name")
    
    # Clean up _buffer_main
    dcc_registry_machinery._buffer_main.remove("test_name")
    assert not dcc_registry_machinery._is_registered("test_name")
    
    # Register name in _buffer_altn and test
    dcc_registry_machinery._buffer_altn.add("test_name")
    assert dcc_registry_machinery._is_registered("test_name")
    
    # Clean up _buffer_altn
    dcc_registry_machinery._buffer_altn.remove("test_name")
    assert not dcc_registry_machinery._is_registered("test_name")
