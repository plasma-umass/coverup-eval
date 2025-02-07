# file: lib/ansible/cli/inventory.py:292-326
# asked: {"lines": [292, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 312, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [299, 301], [302, 303], [302, 307], [304, 302], [304, 305], [307, 308], [307, 310], [311, 312], [311, 314], [321, 322], [321, 326], [323, 321], [323, 324]]}
# gained: {"lines": [292, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 310, 311, 314, 316, 319, 320, 321, 322, 323, 324, 326], "branches": [[299, 300], [299, 301], [302, 303], [302, 307], [304, 305], [307, 308], [311, 314], [321, 322], [321, 326], [323, 324]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def inventory_cli():
    cli = InventoryCLI(MagicMock())
    cli._get_group_variables = MagicMock(return_value={'var1': 'value1'})
    cli._remove_empty = MagicMock()
    cli._get_host_variables = MagicMock(return_value={'hostvar1': 'value1'})
    cli.inventory = MagicMock()
    return cli

def test_json_inventory(inventory_cli, monkeypatch):
    # Mocking context.CLIARGS
    monkeypatch.setattr('ansible.context.CLIARGS', {'export': True, 'basedir': None})

    # Creating mock group and host objects
    mock_host = MagicMock()
    mock_host.name = 'host1'
    mock_group = MagicMock()
    mock_group.name = 'group1'
    mock_group.hosts = [mock_host]
    mock_group.child_groups = []
    mock_top_group = MagicMock()
    mock_top_group.name = 'all'
    mock_top_group.hosts = []
    mock_top_group.child_groups = [mock_group]

    # Mocking inventory.get_hosts
    inventory_cli.inventory.get_hosts = MagicMock(return_value=[mock_host])

    # Running the method
    result = inventory_cli.json_inventory(mock_top_group)

    # Assertions
    assert 'group1' in result
    assert 'hosts' in result['group1']
    assert result['group1']['hosts'] == ['host1']
    assert 'children' in result['group1']
    assert result['group1']['children'] == []
    assert 'vars' in result['group1']
    assert result['group1']['vars'] == {'var1': 'value1'}
    assert '_meta' in result
    assert 'hostvars' in result['_meta']
    assert 'host1' in result['_meta']['hostvars']
    assert result['_meta']['hostvars']['host1'] == {'hostvar1': 'value1'}

    # Ensuring _remove_empty was called
    inventory_cli._remove_empty.assert_called()

    # Clean up
    monkeypatch.undo()
