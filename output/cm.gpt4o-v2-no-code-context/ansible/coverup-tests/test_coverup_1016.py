# file: lib/ansible/plugins/inventory/ini.py:256-266
# asked: {"lines": [262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}
# gained: {"lines": [262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_group_name_valid(inventory_module):
    inventory_module.patterns = {'groupname': MagicMock()}
    inventory_module.patterns['groupname'].match.return_value = MagicMock(group=lambda x: 'group1')
    
    result = inventory_module._parse_group_name('group1')
    assert result == 'group1'

def test_parse_group_name_invalid(inventory_module, mocker):
    inventory_module.patterns = {'groupname': MagicMock()}
    inventory_module.patterns['groupname'].match.return_value = None
    mocker.patch.object(inventory_module, '_raise_error')
    
    inventory_module._parse_group_name('invalid_group')
    inventory_module._raise_error.assert_called_once_with("Expected group name, got: invalid_group")
