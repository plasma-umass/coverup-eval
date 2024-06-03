# file lib/ansible/cli/inventory.py:292-326
# lines [312]
# branches ['299->301', '304->302', '307->310', '311->312', '323->321']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible import context

@pytest.fixture
def mock_cli():
    cli = InventoryCLI(MagicMock())
    cli._get_group_variables = MagicMock(return_value={'var1': 'value1'})
    cli._get_host_variables = MagicMock(return_value={'hostvar1': 'value1'})
    cli._remove_empty = MagicMock()
    cli.inventory = MagicMock()
    return cli

@pytest.fixture
def mock_inventory():
    top_group = Group('all')
    subgroup = Group('subgroup')
    subgroup.hosts = [Host('host1'), Host('host2')]
    top_group.child_groups = [subgroup]
    top_group.hosts = []
    return top_group

def test_json_inventory(mock_cli, mock_inventory, mocker):
    mocker.patch('ansible.context.CLIARGS', {'export': True})
    mocker.patch.object(mock_cli.inventory, 'get_hosts', return_value=[Host('host1'), Host('host2')])

    result = mock_cli.json_inventory(mock_inventory)

    assert 'subgroup' in result
    assert 'hosts' in result['subgroup']
    assert 'children' in result['subgroup']
    assert 'vars' in result['subgroup']
    assert 'host1' in result['_meta']['hostvars']
    assert 'host2' in result['_meta']['hostvars']
    mock_cli._remove_empty.assert_called()
