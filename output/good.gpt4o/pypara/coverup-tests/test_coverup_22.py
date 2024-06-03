# file pypara/dcc.py:310-330
# lines [310, 315, 317, 320, 323, 325, 327, 330]
# branches ['315->317', '315->320', '323->exit', '323->325', '325->327', '325->330']

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry():
    registry = DCCRegistryMachinery()
    registry._buffer_main = {}
    registry._buffer_altn = {}
    return registry

def test_register_dcc(dcc_registry):
    dcc = DCC(name="ACT/360", altnames=["Actual/360", "A/360"], currencies=[], calculate_fraction_method=None)
    
    # Register a new DCC
    dcc_registry.register(dcc)
    
    # Assert that the DCC is registered in the main buffer
    assert dcc_registry._buffer_main["ACT/360"] == dcc
    
    # Assert that the DCC is registered in the alternative buffer
    assert dcc_registry._buffer_altn["Actual/360"] == dcc
    assert dcc_registry._buffer_altn["A/360"] == dcc

def test_register_dcc_name_conflict(dcc_registry):
    dcc1 = DCC(name="ACT/360", altnames=["Actual/360", "A/360"], currencies=[], calculate_fraction_method=None)
    dcc2 = DCC(name="ACT/365", altnames=["Actual/365", "A/360"], currencies=[], calculate_fraction_method=None)
    
    # Register the first DCC
    dcc_registry.register(dcc1)
    
    # Attempt to register a second DCC with a conflicting alternative name
    with pytest.raises(TypeError, match="Day count convention 'ACT/365' is already registered"):
        dcc_registry.register(dcc2)

def test_register_dcc_main_name_conflict(dcc_registry):
    dcc1 = DCC(name="ACT/360", altnames=["Actual/360", "A/360"], currencies=[], calculate_fraction_method=None)
    dcc2 = DCC(name="ACT/360", altnames=["Actual/365", "A/365"], currencies=[], calculate_fraction_method=None)
    
    # Register the first DCC
    dcc_registry.register(dcc1)
    
    # Attempt to register a second DCC with a conflicting main name
    with pytest.raises(TypeError, match="Day count convention 'ACT/360' is already registered"):
        dcc_registry.register(dcc2)
