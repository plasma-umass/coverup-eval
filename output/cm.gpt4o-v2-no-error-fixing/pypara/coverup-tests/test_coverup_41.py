# file: pypara/dcc.py:304-308
# asked: {"lines": [304, 308], "branches": []}
# gained: {"lines": [304, 308], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def dcc_registry():
    return DCCRegistryMachinery()

def test_is_registered_in_main_buffer(dcc_registry):
    dcc_registry._buffer_main['TestDCC'] = 'dummy_value'
    assert dcc_registry._is_registered('TestDCC') is True

def test_is_registered_in_altn_buffer(dcc_registry):
    dcc_registry._buffer_altn['TestDCC'] = 'dummy_value'
    assert dcc_registry._is_registered('TestDCC') is True

def test_is_not_registered(dcc_registry):
    assert dcc_registry._is_registered('NonExistentDCC') is False
