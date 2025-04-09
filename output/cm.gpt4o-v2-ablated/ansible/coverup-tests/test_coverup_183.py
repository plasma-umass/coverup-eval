# file: lib/ansible/cli/inventory.py:246-251
# asked: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}
# gained: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}

import pytest
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def sample_dict():
    return {
        'hosts': {},
        'vars': {},
        'children': {},
        'some_key': 'some_value'
    }

def test_remove_empty_all_keys(sample_dict):
    InventoryCLI._remove_empty(sample_dict)
    assert 'hosts' not in sample_dict
    assert 'vars' not in sample_dict
    assert 'children' not in sample_dict
    assert 'some_key' in sample_dict

def test_remove_empty_some_keys():
    dump = {
        'hosts': {},
        'vars': {'var1': 'value1'},
        'children': {},
        'some_key': 'some_value'
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' not in dump
    assert 'vars' in dump
    assert 'children' not in dump
    assert 'some_key' in dump

def test_remove_empty_no_keys():
    dump = {
        'hosts': {'host1': 'value1'},
        'vars': {'var1': 'value1'},
        'children': {'child1': 'value1'},
        'some_key': 'some_value'
    }
    InventoryCLI._remove_empty(dump)
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' in dump
    assert 'some_key' in dump
