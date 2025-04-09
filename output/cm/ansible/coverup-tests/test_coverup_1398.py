# file lib/ansible/inventory/group.py:244-252
# lines [247]
# branches ['246->247']

import pytest
from ansible.inventory.group import Group
from unittest.mock import MagicMock

@pytest.fixture
def group_with_mocked_set_priority():
    group = Group()
    group.set_priority = MagicMock()
    return group

def test_set_variable_with_group_priority(group_with_mocked_set_priority):
    group = group_with_mocked_set_priority

    # Set a variable with the special key 'ansible_group_priority'
    group.set_variable('ansible_group_priority', '100')

    # Check if set_priority was called with the correct int value
    group.set_priority.assert_called_once_with(100)
