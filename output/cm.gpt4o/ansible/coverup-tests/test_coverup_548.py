# file lib/ansible/plugins/inventory/ini.py:256-266
# lines [256, 262, 263, 264, 266]
# branches ['263->264', '263->266']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.patterns = {'groupname': MagicMock()}
    module._raise_error = MagicMock(side_effect=Exception("Expected group name, got: invalid_group"))
    return module

def test_parse_group_name_success(inventory_module):
    inventory_module.patterns['groupname'].match.return_value = MagicMock(group=MagicMock(return_value='group1'))
    result = inventory_module._parse_group_name('group1')
    assert result == 'group1'

def test_parse_group_name_failure(inventory_module):
    inventory_module.patterns['groupname'].match.return_value = None
    with pytest.raises(Exception, match="Expected group name, got: invalid_group"):
        inventory_module._parse_group_name('invalid_group')
    inventory_module._raise_error.assert_called_once_with("Expected group name, got: invalid_group")
