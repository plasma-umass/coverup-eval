# file lib/ansible/plugins/lookup/inventory_hostnames.py:42-53
# lines [42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53]
# branches ['45->46', '45->50', '47->45', '47->48']

import pytest
from ansible.plugins.lookup.inventory_hostnames import LookupModule
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import patch

@pytest.fixture
def mock_loader():
    return DataLoader()

@pytest.fixture
def mock_variables():
    return {
        'groups': {
            'group1': ['host1', 'host2'],
            'group2': ['host3']
        }
    }

@pytest.fixture
def lookup_module(mock_loader):
    return LookupModule(mock_loader)

def test_run_success(lookup_module, mock_variables):
    terms = 'group1'
    result = lookup_module.run(terms, variables=mock_variables)
    assert result == ['host1', 'host2']

def test_run_no_match(lookup_module, mock_variables):
    terms = 'nonexistent_group'
    result = lookup_module.run(terms, variables=mock_variables)
    assert result == []

def test_run_ansible_error(lookup_module, mock_variables, mocker):
    terms = 'group1'
    mocker.patch.object(InventoryManager, 'get_hosts', side_effect=AnsibleError)
    result = lookup_module.run(terms, variables=mock_variables)
    assert result == []
