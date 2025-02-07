# file: lib/ansible/inventory/helpers.py:29-40
# asked: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}
# gained: {"lines": [29, 36, 37, 38, 40], "branches": [[37, 38], [37, 40]]}

import pytest
from ansible.inventory.helpers import get_group_vars
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars

class MockGroup:
    def __init__(self, name, vars, depth=0, priority=0):
        self.name = name
        self.vars = vars
        self.depth = depth
        self.priority = priority

    def get_vars(self):
        return self.vars.copy()

def test_get_group_vars(monkeypatch):
    # Mock data
    group1 = MockGroup(name="group1", vars={"var1": "value1"}, depth=1, priority=10)
    group2 = MockGroup(name="group2", vars={"var2": "value2"}, depth=2, priority=5)
    groups = [group1, group2]

    # Mock sort_groups to return the groups in a specific order
    def mock_sort_groups(groups):
        return sorted(groups, key=lambda g: (g.depth, g.priority, g.name))

    monkeypatch.setattr("ansible.inventory.helpers.sort_groups", mock_sort_groups)

    # Call the function
    result = get_group_vars(groups)

    # Assertions
    expected_result = {"var1": "value1", "var2": "value2"}
    assert result == expected_result

    # Clean up
    monkeypatch.undo()
