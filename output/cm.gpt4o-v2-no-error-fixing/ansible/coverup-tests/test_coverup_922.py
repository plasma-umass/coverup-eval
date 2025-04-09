# file: lib/ansible/cli/inventory.py:246-251
# asked: {"lines": [], "branches": [[250, 249]]}
# gained: {"lines": [], "branches": [[250, 249]]}

import pytest

from ansible.cli.inventory import InventoryCLI

def test_remove_empty():
    # Test case where 'hosts', 'vars', and 'children' are empty
    dump = {
        'hosts': {},
        'vars': {},
        'children': {}
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' not in dump

    # Test case where 'hosts' is not empty, but 'vars' and 'children' are empty
    dump = {
        'hosts': {'host1': 'value1'},
        'vars': {},
        'children': {}
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' not in dump
    assert 'children' not in dump

    # Test case where 'hosts' and 'vars' are not empty, but 'children' is empty
    dump = {
        'hosts': {'host1': 'value1'},
        'vars': {'var1': 'value1'},
        'children': {}
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' not in dump

    # Test case where none are empty
    dump = {
        'hosts': {'host1': 'value1'},
        'vars': {'var1': 'value1'},
        'children': {'child1': 'value1'}
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' in dump
