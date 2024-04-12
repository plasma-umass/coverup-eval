# file pypara/dcc.py:294-302
# lines [294, 299, 302]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def dcc_registry_machinery():
    return DCCRegistryMachinery()

def test_dcc_registry_machinery_initialization(dcc_registry_machinery):
    assert isinstance(dcc_registry_machinery._buffer_main, dict), "Main buffer should be a dictionary"
    assert isinstance(dcc_registry_machinery._buffer_altn, dict), "Alternative buffer should be a dictionary"
    assert dcc_registry_machinery._buffer_main == {}, "Main buffer should be initialized as an empty dictionary"
    assert dcc_registry_machinery._buffer_altn == {}, "Alternative buffer should be initialized as an empty dictionary"
