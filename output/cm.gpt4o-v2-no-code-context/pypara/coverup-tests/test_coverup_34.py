# file: pypara/dcc.py:355-360
# asked: {"lines": [355, 356, 360], "branches": []}
# gained: {"lines": [355, 356, 360], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry_machinery():
    return DCCRegistryMachinery()

def test_table_property(dcc_registry_machinery, monkeypatch):
    # Mock the _buffer_main and _buffer_altn attributes
    buffer_main = {
        'ACT/360': DCC('ACT/360', altnames=[], currencies=[], calculate_fraction_method=None),
        '30/360': DCC('30/360', altnames=[], currencies=[], calculate_fraction_method=None)
    }
    buffer_altn = {
        'ACT/365': DCC('ACT/365', altnames=[], currencies=[], calculate_fraction_method=None)
    }
    
    monkeypatch.setattr(dcc_registry_machinery, '_buffer_main', buffer_main)
    monkeypatch.setattr(dcc_registry_machinery, '_buffer_altn', buffer_altn)
    
    # Access the table property
    table = dcc_registry_machinery.table
    
    # Assertions to verify the table property
    assert 'ACT/360' in table
    assert '30/360' in table
    assert 'ACT/365' in table
    assert table['ACT/360'] == buffer_main['ACT/360']
    assert table['30/360'] == buffer_main['30/360']
    assert table['ACT/365'] == buffer_altn['ACT/365']
