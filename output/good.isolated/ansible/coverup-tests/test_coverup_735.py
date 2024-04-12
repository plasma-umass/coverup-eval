# file lib/ansible/plugins/inventory/yaml.py:171-177
# lines [171, 175, 177]
# branches []

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

# Mocking the BaseFileInventoryPlugin since we only need to test the InventoryModule's method
class MockedBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def _expand_hostpattern(self, host_pattern):
        # Mock the behavior of _expand_hostpattern to return a tuple
        # Adjust the return value as needed to cover the specific lines/branches
        return ['host1', 'host2'], 22

# The test function to cover InventoryModule._parse_host
def test_parse_host(mocker):
    # Mock the _expand_hostpattern method
    mocker.patch.object(InventoryModule, '_expand_hostpattern', MockedBaseFileInventoryPlugin._expand_hostpattern)

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Define a host pattern to test
    host_pattern = 'host[1:2]'

    # Call the _parse_host method
    hostnames, port = inventory_module._parse_host(host_pattern)

    # Assertions to verify the postconditions
    assert hostnames == ['host1', 'host2']
    assert port == 22

    # No cleanup is necessary as we are using pytest-mock and no external resources are being modified
