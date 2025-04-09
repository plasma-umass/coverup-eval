# file: lib/ansible/cli/inventory.py:292-326
# asked: {"lines": [292, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 312, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [299, 301], [302, 303], [302, 307], [304, 302], [304, 305], [307, 308], [307, 310], [311, 312], [311, 314], [321, 322], [321, 326], [323, 321], [323, 324]]}
# gained: {"lines": [292, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [299, 301], [302, 303], [302, 307], [304, 305], [307, 308], [311, 314], [321, 322], [321, 326], [323, 324]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def inventory_cli():
    cli = InventoryCLI(MagicMock())
    cli.inventory = MagicMock()
    cli.loader = MagicMock()
    cli.vm = MagicMock()
    return cli

@pytest.fixture
def host():
    host = Host(name='test_host')
    host.get_vars = MagicMock(return_value={'var1': 'value1'})
    return host

@pytest.fixture
def group(host):
    group = Group(name='test_group')
    group.hosts = [host]
    group.child_groups = []
    group.get_vars = MagicMock(return_value={'group_var1': 'group_value1'})
    return group

@pytest.fixture
def top_group(group):
    top_group = Group(name='all')
    top_group.hosts = []
    top_group.child_groups = [group]
    return top_group

def test_json_inventory(inventory_cli, top_group, group, host, monkeypatch):
    monkeypatch.setattr('ansible.context.CLIARGS', {'export': True, 'basedir': None})
    
    inventory_cli._get_group_variables = MagicMock(return_value={'group_var1': 'group_value1'})
    inventory_cli._get_host_variables = MagicMock(return_value={'var1': 'value1'})
    inventory_cli._remove_empty = MagicMock()
    inventory_cli.inventory.get_hosts = MagicMock(return_value=[host])
    
    result = inventory_cli.json_inventory(top_group)
    
    assert 'test_group' in result
    assert 'hosts' in result['test_group']
    assert result['test_group']['hosts'] == ['test_host']
    assert 'children' in result['test_group']
    assert result['test_group']['children'] == []
    assert 'vars' in result['test_group']
    assert result['test_group']['vars'] == {'group_var1': 'group_value1'}
    assert '_meta' in result
    assert 'hostvars' in result['_meta']
    assert 'test_host' in result['_meta']['hostvars']
    assert result['_meta']['hostvars']['test_host'] == {'var1': 'value1'}
    
    inventory_cli._remove_empty.assert_called()
    inventory_cli._get_group_variables.assert_any_call(group)
    inventory_cli._get_host_variables.assert_called_with(host)
