# file: lib/ansible/cli/inventory.py:246-251
# asked: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}
# gained: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_remove_empty_with_empty_keys():
    dump = {
        'hosts': {},
        'vars': {},
        'children': {},
        'other': 'value'
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' not in dump
    assert 'other' in dump

def test_remove_empty_with_non_empty_keys():
    dump = {
        'hosts': {'host1': 'value1'},
        'vars': {'var1': 'value1'},
        'children': {'child1': 'value1'},
        'other': 'value'
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' in dump
    assert 'other' in dump

def test_remove_empty_with_mixed_keys():
    dump = {
        'hosts': {},
        'vars': {'var1': 'value1'},
        'children': {},
        'other': 'value'
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' in dump
    assert 'children' not in dump
    assert 'other' in dump
