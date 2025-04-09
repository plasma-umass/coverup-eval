# file lib/ansible/cli/inventory.py:246-251
# lines [246, 247, 249, 250, 251]
# branches ['249->exit', '249->250', '250->249', '250->251']

import pytest
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def mock_inventory_cli(mocker):
    # Mock the required 'args' argument for InventoryCLI
    mock_args = mocker.Mock()
    return InventoryCLI(mock_args)

def test_remove_empty(mock_inventory_cli):
    # Test case where 'hosts', 'vars', and 'children' are empty
    dump = {'hosts': {}, 'vars': {}, 'children': {}}
    mock_inventory_cli._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' not in dump

    # Test case where 'hosts' is not empty
    dump = {'hosts': {'host1': 'value1'}, 'vars': {}, 'children': {}}
    mock_inventory_cli._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' not in dump
    assert 'children' not in dump

    # Test case where 'vars' is not empty
    dump = {'hosts': {}, 'vars': {'var1': 'value1'}, 'children': {}}
    mock_inventory_cli._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' in dump
    assert 'children' not in dump

    # Test case where 'children' is not empty
    dump = {'hosts': {}, 'vars': {}, 'children': {'child1': 'value1'}}
    mock_inventory_cli._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' in dump

    # Test case where none are empty
    dump = {'hosts': {'host1': 'value1'}, 'vars': {'var1': 'value1'}, 'children': {'child1': 'value1'}}
    mock_inventory_cli._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' in dump
