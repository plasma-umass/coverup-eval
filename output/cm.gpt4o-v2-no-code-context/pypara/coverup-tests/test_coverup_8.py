# file: pypara/dcc.py:310-330
# asked: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}
# gained: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

class MockDCC:
    def __init__(self, name, altnames):
        self.name = name
        self.altnames = altnames

@pytest.fixture
def dcc_registry():
    registry = DCCRegistryMachinery()
    registry._buffer_main = {}
    registry._buffer_altn = {}
    return registry

def test_register_main_name_already_registered(dcc_registry):
    dcc1 = MockDCC(name="30/360", altnames=["30E/360", "360/360"])
    dcc_registry._buffer_main[dcc1.name] = dcc1

    dcc2 = MockDCC(name="30/360", altnames=["ACT/360"])
    with pytest.raises(TypeError, match="Day count convention '30/360' is already registered"):
        dcc_registry.register(dcc2)

def test_register_alt_name_already_registered(dcc_registry):
    dcc1 = MockDCC(name="30/360", altnames=["30E/360", "360/360"])
    dcc_registry._buffer_main[dcc1.name] = dcc1
    dcc_registry._buffer_altn["30E/360"] = dcc1

    dcc2 = MockDCC(name="ACT/360", altnames=["30E/360"])
    with pytest.raises(TypeError, match="Day count convention 'ACT/360' is already registered"):
        dcc_registry.register(dcc2)

def test_register_success(dcc_registry):
    dcc = MockDCC(name="30/360", altnames=["30E/360", "360/360"])
    dcc_registry.register(dcc)

    assert dcc_registry._buffer_main["30/360"] == dcc
    assert dcc_registry._buffer_altn["30E/360"] == dcc
    assert dcc_registry._buffer_altn["360/360"] == dcc
