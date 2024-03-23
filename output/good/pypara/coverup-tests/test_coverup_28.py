# file pypara/dcc.py:348-353
# lines [348, 349, 353]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

class MockDCC:
    pass

@pytest.fixture
def dcc_registry_machinery():
    machinery = DCCRegistryMachinery()
    machinery._buffer_main = {'mock': MockDCC()}
    yield machinery
    # Cleanup code if necessary

def test_registry_property(dcc_registry_machinery):
    registry = dcc_registry_machinery.registry
    assert isinstance(registry, list)
    assert len(registry) == 1
    assert isinstance(registry[0], MockDCC)
