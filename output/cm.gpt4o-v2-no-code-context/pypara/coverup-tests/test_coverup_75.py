# file: pypara/dcc.py:332-336
# asked: {"lines": [332, 336], "branches": []}
# gained: {"lines": [332, 336], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def dcc_registry():
    class MockDCC:
        pass

    registry = DCCRegistryMachinery()
    registry._buffer_main = {}
    registry._buffer_altn = {}
    registry._buffer_main['main_dcc'] = MockDCC()
    registry._buffer_altn['altn_dcc'] = MockDCC()
    registry.MockDCC = MockDCC  # Attach MockDCC to the registry for testing purposes
    return registry

def test_find_strict_main_buffer(dcc_registry):
    result = dcc_registry._find_strict('main_dcc')
    assert result is not None
    assert isinstance(result, dcc_registry.MockDCC)

def test_find_strict_altn_buffer(dcc_registry):
    result = dcc_registry._find_strict('altn_dcc')
    assert result is not None
    assert isinstance(result, dcc_registry.MockDCC)

def test_find_strict_not_found(dcc_registry):
    result = dcc_registry._find_strict('non_existent_dcc')
    assert result is None
