# file lib/ansible/inventory/group.py:254-258
# lines [254, 256, 257, 258]
# branches ['257->exit', '257->258']

import pytest
from ansible.inventory.group import Group

# Mock Group class to add get_ancestors method
class MockGroup(Group):
    def get_ancestors(self):
        return self.ancestors

# Test function to improve coverage
def test_clear_hosts_cache(mocker):
    # Create a mock ancestor group
    ancestor_group = mocker.MagicMock(spec=Group)
    ancestor_group._hosts_cache = ['host1', 'host2']

    # Create a group with mocked ancestor
    group = MockGroup()
    group._hosts_cache = ['host3', 'host4']
    group.ancestors = [ancestor_group]

    # Clear hosts cache
    group.clear_hosts_cache()

    # Assertions to verify postconditions
    assert group._hosts_cache is None, "Group's hosts cache should be cleared"
    assert ancestor_group._hosts_cache is None, "Ancestor's hosts cache should be cleared"

    # Cleanup is not necessary as we are using mocks and not affecting any real objects or state
