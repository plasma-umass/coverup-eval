# file: lib/ansible/cli/inventory.py:365-404
# asked: {"lines": [366, 367, 369, 370, 371, 373, 374, 375, 376, 377, 378, 379, 381, 382, 383, 384, 385, 387, 388, 389, 390, 391, 393, 394, 396, 397, 398, 400, 402, 404], "branches": [[374, 375], [374, 381], [375, 376], [375, 377], [377, 378], [377, 379], [381, 382], [381, 393], [382, 383], [382, 393], [383, 384], [383, 387], [393, 394], [393, 396], [397, 398], [397, 400]]}
# gained: {"lines": [366, 367, 369, 370, 371, 373, 374, 375, 377, 379, 381, 382, 383, 384, 385, 388, 389, 390, 391, 393, 394, 396, 397, 400, 402, 404], "branches": [[374, 375], [374, 381], [375, 377], [377, 379], [381, 382], [381, 393], [382, 383], [382, 393], [383, 384], [393, 394], [397, 400]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def mock_top():
    class MockHost:
        def __init__(self, name):
            self.name = name

    class MockGroup:
        def __init__(self, name, hosts=None, child_groups=None):
            self.name = name
            self.hosts = hosts or []
            self.child_groups = child_groups or []

    ungrouped_host = MockHost('ungrouped_host')
    other_host = MockHost('other_host')
    ungrouped_group = MockGroup('ungrouped', hosts=[ungrouped_host])
    other_group = MockGroup('other', hosts=[other_host])
    all_group = MockGroup('all', child_groups=[ungrouped_group, other_group])

    return all_group

@pytest.fixture
def inventory_cli():
    return InventoryCLI(args=['inventory'])

def test_toml_inventory(inventory_cli, mock_top, monkeypatch):
    # Mocking methods
    monkeypatch.setattr(inventory_cli, '_get_host_variables', lambda host: {'var': 'value'})
    monkeypatch.setattr(inventory_cli, '_get_group_variables', lambda group: {'group_var': 'value'})
    monkeypatch.setattr(inventory_cli, '_remove_empty', lambda x: x.pop('empty', None))
    monkeypatch.setattr('ansible.context.CLIARGS', {'export': True})

    result = inventory_cli.toml_inventory(mock_top)

    assert 'all' in result
    assert 'ungrouped' in result
    assert 'other' in result
    assert 'ungrouped_host' in result['ungrouped']['hosts']
    assert 'other_host' in result['other']['hosts']
    assert result['ungrouped']['hosts']['ungrouped_host'] == {'var': 'value'}
    assert result['other']['hosts']['other_host'] == {'var': 'value'}
    assert result['ungrouped']['vars'] == {'group_var': 'value'}
    assert result['other']['vars'] == {'group_var': 'value'}
