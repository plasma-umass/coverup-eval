# file: pypara/dcc.py:304-308
# asked: {"lines": [304, 308], "branches": []}
# gained: {"lines": [304, 308], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def registry():
    return DCCRegistryMachinery()

def test_is_registered_in_main_buffer(registry):
    registry._buffer_main['test_name'] = 'test_value'
    assert registry._is_registered('test_name') is True

def test_is_registered_in_altn_buffer(registry):
    registry._buffer_altn['test_name'] = 'test_value'
    assert registry._is_registered('test_name') is True

def test_is_not_registered(registry):
    assert registry._is_registered('non_existent_name') is False
