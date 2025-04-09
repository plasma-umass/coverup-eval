# file: lib/ansible/cli/inventory.py:246-251
# asked: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}
# gained: {"lines": [246, 247, 249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_remove_empty():
    dump = {
        'hosts': [],
        'vars': {},
        'children': {},
        'other': 'value'
    }
    
    InventoryCLI._remove_empty(dump)
    
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' not in dump
    assert 'other' in dump
    assert dump['other'] == 'value'

def test_remove_empty_no_empty_keys():
    dump = {
        'hosts': ['host1'],
        'vars': {'var1': 'value1'},
        'children': {'child1': 'value1'},
        'other': 'value'
    }
    
    InventoryCLI._remove_empty(dump)
    
    assert 'hosts' in dump
    assert 'vars' in dump
    assert 'children' in dump
    assert 'other' in dump
    assert dump['hosts'] == ['host1']
    assert dump['vars'] == {'var1': 'value1'}
    assert dump['children'] == {'child1': 'value1'}
    assert dump['other'] == 'value'
