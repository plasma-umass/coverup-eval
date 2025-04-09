# file: pypara/dcc.py:348-353
# asked: {"lines": [348, 349, 353], "branches": []}
# gained: {"lines": [348, 349, 353], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming DCCRegistryMachinery and DCC are imported from pypara.dcc
from pypara.dcc import DCCRegistryMachinery

class TestDCCRegistryMachinery:
    
    @pytest.fixture
    def dcc_registry_machinery(self):
        # Create an instance of DCCRegistryMachinery
        return DCCRegistryMachinery()

    def test_registry_property(self, dcc_registry_machinery, mocker):
        # Mock the _buffer_main attribute
        mock_buffer_main = {'key1': 'value1', 'key2': 'value2'}
        mocker.patch.object(dcc_registry_machinery, '_buffer_main', mock_buffer_main)
        
        # Access the registry property
        registry = dcc_registry_machinery.registry
        
        # Assert that the registry property returns the correct list of values
        assert registry == list(mock_buffer_main.values())
