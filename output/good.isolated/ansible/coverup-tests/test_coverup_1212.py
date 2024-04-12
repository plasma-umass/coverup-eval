# file lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# lines [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53]
# branches ['45->46', '45->50', '47->45', '47->48']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.plugins.lookup.inventory_hostnames import LookupModule
from unittest.mock import MagicMock

# Mock the InventoryManager to raise AnsibleError when get_hosts is called
@pytest.fixture
def inventory_manager_raise_error(mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager.get_hosts', side_effect=AnsibleError)

# Test function to cover the exception branch
def test_lookup_inventory_hostnames_exception(inventory_manager_raise_error):
    lookup = LookupModule()
    lookup._loader = MagicMock()
    variables = {
        'groups': {
            'test_group': ['host1', 'host2']
        }
    }
    terms = 'test_group'
    result = lookup.run(terms, variables)
    assert result == [], "Expected an empty list when AnsibleError is raised"
