# file lib/ansible/plugins/inventory/ini.py:256-266
# lines [262, 263, 264, 266]
# branches ['263->264', '263->266']

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError
from unittest.mock import MagicMock

@pytest.fixture
def inventory_module(mocker):
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin.__init__', return_value=None)
    inventory_module = InventoryModule()
    inventory_module._raise_error = MagicMock(side_effect=AnsibleParserError)
    inventory_module.patterns = {'groupname': mocker.MagicMock()}
    return inventory_module

def test_parse_group_name_success(inventory_module, mocker):
    group_name = 'mygroup'
    match_mock = mocker.MagicMock()
    match_mock.group.return_value = group_name
    inventory_module.patterns['groupname'].match.return_value = match_mock
    assert inventory_module._parse_group_name('[{}]'.format(group_name)) == group_name

def test_parse_group_name_failure(inventory_module):
    inventory_module.patterns['groupname'].match.return_value = None
    with pytest.raises(AnsibleParserError):
        inventory_module._parse_group_name('[invalid-group]')
