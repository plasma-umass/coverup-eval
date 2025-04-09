# file: lib/ansible/plugins/inventory/ini.py:256-266
# asked: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}
# gained: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.inventory.ini import InventoryModule

@pytest.fixture
def inventory_module(mocker):
    module = InventoryModule()
    module._filename = "testfile.ini"
    module.lineno = 1
    module.patterns = {'groupname': mocker.Mock()}
    return module

def test_parse_group_name_success(inventory_module, mocker):
    line = "[groupname]"
    match_mock = mocker.Mock()
    match_mock.group.return_value = "groupname"
    inventory_module.patterns['groupname'].match.return_value = match_mock

    result = inventory_module._parse_group_name(line)
    assert result == "groupname"

def test_parse_group_name_failure(inventory_module, mocker):
    line = "not_a_groupname"
    inventory_module.patterns['groupname'].match.return_value = None

    with pytest.raises(AnsibleError, match="Expected group name, got: not_a_groupname"):
        inventory_module._parse_group_name(line)
