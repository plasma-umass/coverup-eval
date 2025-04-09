# file lib/ansible/cli/inventory.py:246-251
# lines [246, 247, 249, 250, 251]
# branches ['249->exit', '249->250', '250->249', '250->251']

import pytest
from ansible.cli.inventory import InventoryCLI

def test_remove_empty():
    # Setup a dictionary with empty keys
    data_with_empty_keys = {
        'hosts': {},
        'vars': {},
        'children': {},
        'non_empty': 'value'
    }

    # Call the static method to remove empty keys
    InventoryCLI._remove_empty(data_with_empty_keys)

    # Assert that the empty keys have been removed
    assert 'hosts' not in data_with_empty_keys
    assert 'vars' not in data_with_empty_keys
    assert 'children' not in data_with_empty_keys
    assert 'non_empty' in data_with_empty_keys
    assert data_with_empty_keys['non_empty'] == 'value'

    # Setup a dictionary without empty keys
    data_without_empty_keys = {
        'hosts': {'host1': 'value1'},
        'vars': {'var1': 'value1'},
        'children': {'child1': 'value1'},
        'non_empty': 'value'
    }

    # Call the static method to remove empty keys
    InventoryCLI._remove_empty(data_without_empty_keys)

    # Assert that no keys have been removed
    assert 'hosts' in data_without_empty_keys
    assert 'vars' in data_without_empty_keys
    assert 'children' in data_without_empty_keys
    assert 'non_empty' in data_without_empty_keys
    assert data_without_empty_keys['non_empty'] == 'value'
