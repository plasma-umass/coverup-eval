# file: lib/ansible/plugins/inventory/constructed.py:115-117
# asked: {"lines": [115, 117], "branches": []}
# gained: {"lines": [115, 117], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.utils.vars import combine_vars

@pytest.fixture
def inventory_module():
    return InventoryModule()

@pytest.fixture
def mock_host():
    host = Mock()
    host.get_groups.return_value = ['group1', 'group2']
    host.get_vars.return_value = {'var1': 'value1'}
    return host

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_sources():
    return Mock()

def test_get_all_host_vars(inventory_module, mock_host, mock_loader, mock_sources):
    with patch.object(inventory_module, 'get_option', return_value=False):
        with patch.object(inventory_module, 'host_groupvars', return_value={'group_var1': 'group_value1'}) as mock_host_groupvars:
            with patch.object(inventory_module, 'host_vars', return_value={'host_var1': 'host_value1'}) as mock_host_vars:
                result = inventory_module.get_all_host_vars(mock_host, mock_loader, mock_sources)
                expected = combine_vars({'group_var1': 'group_value1'}, {'host_var1': 'host_value1'})
                assert result == expected
                mock_host_groupvars.assert_called_once_with(mock_host, mock_loader, mock_sources)
                mock_host_vars.assert_called_once_with(mock_host, mock_loader, mock_sources)
