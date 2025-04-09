# file: lib/ansible/inventory/helpers.py:29-40
# asked: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}
# gained: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}

import pytest
from ansible.inventory.helpers import get_group_vars
from ansible.inventory.group import Group

class MockGroup:
    def __init__(self, vars, depth=0, priority=0, name=""):
        self.vars = vars
        self.depth = depth
        self.priority = priority
        self.name = name

    def get_vars(self):
        return self.vars

def test_get_group_vars(monkeypatch):
    # Mocking sort_groups to return the groups in a specific order
    def mock_sort_groups(groups):
        return sorted(groups, key=lambda g: (g.depth, g.priority, g.name))

    monkeypatch.setattr('ansible.inventory.helpers.sort_groups', mock_sort_groups)

    group1 = MockGroup({'var1': 'value1'}, depth=1, priority=1, name='group1')
    group2 = MockGroup({'var2': 'value2'}, depth=2, priority=2, name='group2')
    groups = [group2, group1]

    result = get_group_vars(groups)
    expected = {'var1': 'value1', 'var2': 'value2'}

    assert result == expected
