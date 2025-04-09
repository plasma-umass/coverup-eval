# file pypara/dcc.py:332-336
# lines [332, 336]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery
from typing import Optional

# Assuming DCC is a class within the pypara.dcc module
# and requires 'name', 'altnames', 'currencies', and 'calculate_fraction_method' arguments for instantiation
from pypara.dcc import DCC

@pytest.fixture
def dcc_registry_machinery():
    registry = DCCRegistryMachinery()
    registry._buffer_main = {}
    registry._buffer_altn = {}
    return registry

def test_find_strict_none(dcc_registry_machinery):
    assert dcc_registry_machinery._find_strict("nonexistent") is None

def test_find_strict_main(dcc_registry_machinery):
    dcc = DCC(name="existent_main", altnames=[], currencies=[], calculate_fraction_method=lambda x, y: 0)
    dcc_registry_machinery._buffer_main["existent_main"] = dcc
    assert dcc_registry_machinery._find_strict("existent_main") is dcc

def test_find_strict_altn(dcc_registry_machinery):
    dcc = DCC(name="existent_altn", altnames=[], currencies=[], calculate_fraction_method=lambda x, y: 0)
    dcc_registry_machinery._buffer_altn["existent_altn"] = dcc
    assert dcc_registry_machinery._find_strict("existent_altn") is dcc
