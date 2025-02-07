# file: pypara/dcc.py:338-346
# asked: {"lines": [346], "branches": []}
# gained: {"lines": [346], "branches": []}

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
    dcc = MagicMock(spec=DCC)
    dcc_registry._buffer_main['EXACT'] = dcc
    dcc_registry._find_strict = MagicMock(return_value=dcc)
    result = dcc_registry.find('EXACT')
    assert result == dcc

def test_find_with_stripped_uppercase_name(dcc_registry):
    dcc = MagicMock(spec=DCC)
    dcc_registry._buffer_altn['STRIPPED'] = dcc
    dcc_registry._find_strict = MagicMock(side_effect=[None, dcc])
    result = dcc_registry.find('  stripped  ')
    assert result == dcc

def test_find_with_nonexistent_name(dcc_registry):
    dcc_registry._find_strict = MagicMock(return_value=None)
    result = dcc_registry.find('NONEXISTENT')
    assert result is None
