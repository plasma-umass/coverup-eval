# file lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# lines [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53]
# branches ['45->46', '45->50', '47->45', '47->48']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.plugins.loader import lookup_loader
from ansible.plugins.lookup.inventory_hostnames import LookupModule

# Mock the InventoryManager to raise AnsibleError when get_hosts is called
class MockedInventoryManager(InventoryManager):
    def get_hosts(self, pattern=None):
        raise AnsibleError("Mocked exception")

# Test function to improve coverage
def test_lookup_inventory_hostnames_exception_handling(mocker):
    # Mock the InventoryManager to use our MockedInventoryManager
    mocker.patch('ansible.plugins.lookup.inventory_hostnames.InventoryManager', new=MockedInventoryManager)

    # Create an instance of our LookupModule
    lookup = LookupModule(loader=None)

    # Define the variables with groups and hosts
    variables = {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3'],
        }
    }

    # Run the lookup plugin with a term that will trigger the exception
    result = lookup.run(terms='*', variables=variables)

    # Assert that the result is an empty list due to the exception
    assert result == [], "Expected an empty list when an AnsibleError is raised"
