# file: lib/ansible/cli/inventory.py:253-258
# asked: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}
# gained: {"lines": [253, 254, 255, 256, 257, 258], "branches": [[256, 257], [256, 258]]}

import pytest
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def sample_dump():
    return {'var1': 'value1', 'var2': 'value2'}

def test_show_vars(sample_dump):
    result = InventoryCLI._show_vars(sample_dump, 1)
    expected = ['  |--{var1 = value1}', '  |--{var2 = value2}']
    assert result == expected

def test_show_vars_empty():
    result = InventoryCLI._show_vars({}, 1)
    assert result == []
