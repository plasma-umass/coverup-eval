# file: lib/ansible/cli/inventory.py:253-258
# asked: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}
# gained: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}

import pytest
from ansible.cli.inventory import InventoryCLI

def test_show_vars(monkeypatch):
    dump = {'var1': 'value1', 'var2': 'value2'}
    depth = 1

    def mock_graph_name(name, depth):
        return f"mocked_{name}_{depth}"

    monkeypatch.setattr(InventoryCLI, '_graph_name', mock_graph_name)

    result = InventoryCLI._show_vars(dump, depth)
    expected_result = [
        'mocked_{var1 = value1}_1',
        'mocked_{var2 = value2}_1'
    ]

    assert result == expected_result
