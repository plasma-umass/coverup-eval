# file: lib/ansible/plugins/inventory/ini.py:256-266
# asked: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}
# gained: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}

import pytest
import re
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module():
    module = InventoryModule()
    module.patterns = {'groupname': re.compile(r'^\[(.+)\]$')}
    return module

def test_parse_group_name_valid(inventory_module):
    line = "[group1]"
    group_name = inventory_module._parse_group_name(line)
    assert group_name == "group1"

def test_parse_group_name_invalid(inventory_module, mocker):
    line = "invalid_group"
    mocker.patch.object(inventory_module, '_raise_error')
    inventory_module._parse_group_name(line)
    inventory_module._raise_error.assert_called_once_with("Expected group name, got: invalid_group")
