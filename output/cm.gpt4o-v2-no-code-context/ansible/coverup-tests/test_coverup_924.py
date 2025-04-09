# file: lib/ansible/cli/inventory.py:292-326
# asked: {"lines": [294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 312, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [299, 301], [302, 303], [302, 307], [304, 302], [304, 305], [307, 308], [307, 310], [311, 312], [311, 314], [321, 322], [321, 326], [323, 321], [323, 324]]}
# gained: {"lines": [294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [302, 303], [302, 307], [304, 305], [307, 308], [307, 310], [311, 314], [321, 322], [321, 326], [323, 324]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from operator import attrgetter

@pytest.fixture
def mock_inventory():
    inventory = MagicMock()
    host1 = Host(name='host1')
    host2 = Host(name='host2')
    group1 = Group(name='group1')
    group2 = Group(name='group2')
    group1.add_host(host1)
    group1.add_child_group(group2)
    group2.add_host(host2)
    inventory.get_hosts.return_value = [host1, host2]
    return inventory, group1

@pytest.fixture
def mock_cli(mock_inventory):
    inventory, top_group = mock_inventory
    cli = InventoryCLI(args=['inventory'])
    cli.inventory = inventory
    cli._get_group_variables = MagicMock(return_value={'var1': 'value1'})
    cli._get_host_variables = MagicMock(return_value={'hostvar1': 'hostvalue1'})
    cli._remove_empty = MagicMock()
    return cli, top_group

def test_json_inventory(mock_cli):
    cli, top_group = mock_cli

    with patch('ansible.cli.inventory.context.CLIARGS', {'export': True}):
        result = cli.json_inventory(top_group)

    assert 'group1' in result
    assert 'hosts' in result['group1']
    assert 'children' in result['group1']
    assert 'group2' in result
    assert 'hosts' in result['group2']
    assert 'vars' in result['group1']
    assert '_meta' in result
    assert 'hostvars' in result['_meta']
    assert 'host1' in result['_meta']['hostvars']
    assert 'host2' in result['_meta']['hostvars']

def test_json_inventory_no_export(mock_cli):
    cli, top_group = mock_cli

    with patch('ansible.cli.inventory.context.CLIARGS', {'export': False}):
        result = cli.json_inventory(top_group)

    assert 'group1' in result
    assert 'hosts' in result['group1']
    assert 'children' in result['group1']
    assert 'group2' in result
    assert 'hosts' in result['group2']
    assert 'vars' not in result['group1']
    assert '_meta' in result
    assert 'hostvars' in result['_meta']
    assert 'host1' in result['_meta']['hostvars']
    assert 'host2' in result['_meta']['hostvars']
