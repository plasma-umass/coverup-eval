# file: lib/ansible/cli/inventory.py:246-251
# asked: {"lines": [249, 250, 251], "branches": [[249, 0], [249, 250], [250, 249], [250, 251]]}
# gained: {"lines": [249, 250, 251], "branches": [[249, 0], [249, 250], [250, 251]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_remove_empty():
    dump = {
        'hosts': [],
        'vars': {},
        'children': {},
        'other': 'data'
    }
    
    InventoryCLI._remove_empty(dump)
    
    assert 'hosts' not in dump
    assert 'vars' not in dump
    assert 'children' not in dump
    assert 'other' in dump
    assert dump['other'] == 'data'
