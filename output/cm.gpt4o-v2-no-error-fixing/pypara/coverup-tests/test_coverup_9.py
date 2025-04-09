# file: pypara/dcc.py:310-330
# asked: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}
# gained: {"lines": [310, 315, 317, 320, 323, 325, 327, 330], "branches": [[315, 317], [315, 320], [323, 0], [323, 325], [325, 327], [325, 330]]}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry():
    return DCCRegistryMachinery()

@pytest.fixture
def dcc():
    return DCC(
        name="30/360",
        altnames={"30U/360", "30/360 US"},
        currencies=set(),
        calculate_fraction_method=None
    )

def test_register_new_dcc(dcc_registry, dcc):
    dcc_registry.register(dcc)
    assert dcc_registry._buffer_main[dcc.name] == dcc
    for altname in dcc.altnames:
        assert dcc_registry._buffer_altn[altname] == dcc

def test_register_existing_main_name(dcc_registry, dcc):
    dcc_registry.register(dcc)
    with pytest.raises(TypeError, match=f"Day count convention '{dcc.name}' is already registered"):
        dcc_registry.register(dcc)

def test_register_existing_alt_name(dcc_registry, dcc):
    dcc_registry.register(dcc)
    new_dcc = DCC(
        name="30/360 ISDA",
        altnames={"30/360 US"},
        currencies=set(),
        calculate_fraction_method=None
    )
    with pytest.raises(TypeError, match=f"Day count convention '{new_dcc.name}' is already registered"):
        dcc_registry.register(new_dcc)
