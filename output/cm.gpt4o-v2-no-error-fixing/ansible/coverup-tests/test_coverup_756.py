# file: lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# asked: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}
# gained: {"lines": [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53], "branches": [[45, 46], [45, 50], [47, 45], [47, 48]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.plugins.lookup.inventory_hostnames import LookupModule

@pytest.fixture
def inventory_data():
    return {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }

def test_lookup_module_run_success(monkeypatch, inventory_data):
    def mock_get_hosts(self, pattern='all', ignore_limits=False, ignore_restrictions=False, order=None):
        class MockHost:
            def __init__(self, name):
                self.name = name
        return [MockHost('host1'), MockHost('host2')]

    monkeypatch.setattr(InventoryManager, 'get_hosts', mock_get_hosts)

    lookup = LookupModule()
    result = lookup.run('group1', variables=inventory_data)
    assert result == ['host1', 'host2']

def test_lookup_module_run_ansible_error(monkeypatch, inventory_data):
    def mock_get_hosts(self, pattern='all', ignore_limits=False, ignore_restrictions=False, order=None):
        raise AnsibleError("Test error")

    monkeypatch.setattr(InventoryManager, 'get_hosts', mock_get_hosts)

    lookup = LookupModule()
    result = lookup.run('group1', variables=inventory_data)
    assert result == []
