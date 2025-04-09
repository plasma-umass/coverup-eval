# file: pypara/dcc.py:294-302
# asked: {"lines": [294, 299, 302], "branches": []}
# gained: {"lines": [294, 299, 302], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery

def test_dcc_registry_machinery_init():
    registry = DCCRegistryMachinery()
    assert registry._buffer_main == {}
    assert registry._buffer_altn == {}
