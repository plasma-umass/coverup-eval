# file pypara/dcc.py:338-346
# lines [338, 346]
# branches []

import pytest
from unittest.mock import MagicMock
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry_machinery():
    return DCCRegistryMachinery()

def test_find_with_exact_name(dcc_registry_machinery, mocker):
    mock_dcc = MagicMock(spec=DCC)
    mocker.patch.object(dcc_registry_machinery, '_find_strict', side_effect=lambda name: mock_dcc if name == "EXACT" else None)
    
    result = dcc_registry_machinery.find("EXACT")
    
    assert result == mock_dcc

def test_find_with_stripped_uppercased_name(dcc_registry_machinery, mocker):
    mock_dcc = MagicMock(spec=DCC)
    mocker.patch.object(dcc_registry_machinery, '_find_strict', side_effect=lambda name: mock_dcc if name == "EXACT" else None)
    
    result = dcc_registry_machinery.find("  exact  ")
    
    assert result == mock_dcc

def test_find_with_nonexistent_name(dcc_registry_machinery, mocker):
    mocker.patch.object(dcc_registry_machinery, '_find_strict', return_value=None)
    
    result = dcc_registry_machinery.find("NONEXISTENT")
    
    assert result is None
