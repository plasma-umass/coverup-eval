# file pypara/dcc.py:310-330
# lines [310, 315, 317, 320, 323, 325, 327, 330]
# branches ['315->317', '315->320', '323->exit', '323->325', '325->327', '325->330']

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC

@pytest.fixture
def registry_machinery():
    class DCCRegistryMachineryMock(DCCRegistryMachinery):
        def __init__(self):
            self._buffer_main = {}
            self._buffer_altn = {}

        def _is_registered(self, name):
            return name in self._buffer_main or name in self._buffer_altn

    return DCCRegistryMachineryMock()

@pytest.fixture
def dcc():
    return DCC(name='DCC1', altnames=['DCC1_ALT'], currencies=['USD'], calculate_fraction_method=lambda start, end: 0)

def test_register_dcc(registry_machinery, dcc):
    # Register the DCC for the first time
    registry_machinery.register(dcc)
    assert dcc.name in registry_machinery._buffer_main
    assert dcc.altnames[0] in registry_machinery._buffer_altn

    # Attempt to register the same DCC again
    with pytest.raises(TypeError) as excinfo:
        registry_machinery.register(dcc)
    assert str(excinfo.value) == f"Day count convention '{dcc.name}' is already registered"

    # Create a new DCC with a conflicting alternative name
    dcc_conflict = DCC(name='DCC2', altnames=['DCC1_ALT'], currencies=['EUR'], calculate_fraction_method=lambda start, end: 0)
    with pytest.raises(TypeError) as excinfo:
        registry_machinery.register(dcc_conflict)
    assert str(excinfo.value) == f"Day count convention '{dcc_conflict.name}' is already registered"
