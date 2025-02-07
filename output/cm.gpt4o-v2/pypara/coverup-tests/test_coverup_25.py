# file: pypara/dcc.py:348-353
# asked: {"lines": [348, 349, 353], "branches": []}
# gained: {"lines": [348, 349, 353], "branches": []}

import pytest
from pypara.dcc import DCCRegistryMachinery, DCC
from decimal import Decimal
from typing import Set
from pypara.currencies import Currency

def test_registry_property():
    # Setup
    registry_machinery = DCCRegistryMachinery()
    dcc = DCC(
        name="TestDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=None
    )
    registry_machinery._buffer_main["TestDCC"] = dcc

    # Exercise
    registry = registry_machinery.registry

    # Verify
    assert registry == [dcc]

    # Cleanup
    del registry_machinery._buffer_main["TestDCC"]
