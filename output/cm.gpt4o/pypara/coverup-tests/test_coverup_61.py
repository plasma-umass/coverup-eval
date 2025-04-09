# file pypara/dcc.py:304-308
# lines [304, 308]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the DCCRegistryMachinery class is imported from pypara.dcc
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def dcc_registry():
    registry = DCCRegistryMachinery()
    registry._buffer_main = set()
    registry._buffer_altn = set()
    return registry

def test_is_registered_main_buffer(dcc_registry):
    dcc_registry._buffer_main.add("test_name")
    assert dcc_registry._is_registered("test_name") is True

def test_is_registered_altn_buffer(dcc_registry):
    dcc_registry._buffer_altn.add("test_name")
    assert dcc_registry._is_registered("test_name") is True

def test_is_not_registered(dcc_registry):
    assert dcc_registry._is_registered("test_name") is False
