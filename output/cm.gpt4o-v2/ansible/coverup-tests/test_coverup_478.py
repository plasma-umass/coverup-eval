# file: lib/ansible/cli/inventory.py:253-258
# asked: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}
# gained: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_show_vars():
    dump = {'var1': 'value1', 'var2': 'value2'}
    depth = 1
    expected_result = [
        InventoryCLI._graph_name('{var1 = value1}', depth),
        InventoryCLI._graph_name('{var2 = value2}', depth)
    ]
    
    result = InventoryCLI._show_vars(dump, depth)
    
    assert result == expected_result

def test_show_vars_empty():
    dump = {}
    depth = 1
    expected_result = []
    
    result = InventoryCLI._show_vars(dump, depth)
    
    assert result == expected_result
