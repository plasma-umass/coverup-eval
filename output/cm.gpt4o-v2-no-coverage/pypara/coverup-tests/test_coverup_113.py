# file: pypara/dcc.py:338-346
# asked: {"lines": [338, 346], "branches": []}
# gained: {"lines": [338, 346], "branches": []}

import pytest
from unittest.mock import MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry():
    registry = DCCRegistryMachinery()
    registry._buffer_main = {}
    registry._buffer_altn = {}
    return registry

def test_find_with_exact_name(dcc_registry):
    dcc = DCC(name="EXACT", altnames=set(), currencies=set(), calculate_fraction_method=MagicMock())
    dcc_registry._buffer_main['EXACT'] = dcc
    result = dcc_registry.find('EXACT')
    assert result is dcc

def test_find_with_stripped_uppercase_name(dcc_registry):
    dcc = DCC(name="EXACT", altnames=set(), currencies=set(), calculate_fraction_method=MagicMock())
    dcc_registry._buffer_altn['EXACT'] = dcc
    result = dcc_registry.find('  exact  ')
    assert result is dcc

def test_find_with_nonexistent_name(dcc_registry):
    result = dcc_registry.find('NONEXISTENT')
    assert result is None
