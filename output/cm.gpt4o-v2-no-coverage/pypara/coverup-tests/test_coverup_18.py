# file: pypara/dcc.py:348-353
# asked: {"lines": [348, 349, 353], "branches": []}
# gained: {"lines": [348, 349, 353], "branches": []}

import pytest
from unittest.mock import MagicMock

def test_registry_property():
    from pypara.dcc import DCCRegistryMachinery

    # Create an instance of DCCRegistryMachinery
    dcc_registry = DCCRegistryMachinery()

    # Mock the _buffer_main attribute
    dcc_registry._buffer_main = MagicMock()
    dcc_registry._buffer_main.values.return_value = ['dcc1', 'dcc2', 'dcc3']

    # Access the registry property
    registry_values = dcc_registry.registry

    # Assert the registry property returns the correct values
    assert registry_values == ['dcc1', 'dcc2', 'dcc3']

    # Clean up
    del dcc_registry._buffer_main

