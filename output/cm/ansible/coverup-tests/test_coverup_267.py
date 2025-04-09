# file lib/ansible/inventory/host.py:105-113
# lines [105, 107, 108, 109, 111, 112, 113]
# branches ['107->108', '107->111', '108->exit', '108->109', '111->exit', '111->112', '112->111', '112->113']

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def mock_host(mocker):
    mocker.patch('ansible.inventory.host.Host.add_group')

def test_populate_ancestors_with_additions(mock_host):
    host = Host(name='testhost')
    group1 = Group(name='group1')
    group2 = Group(name='group2')
    host.groups = [group1]

    # Call populate_ancestors with additions that include a new group
    host.populate_ancestors(additions=[group1, group2])

    # Verify that the new group is added to the host's groups
    assert group2 in host.groups
    # Verify that the existing group is not added again
    assert host.groups.count(group1) == 1

def test_populate_ancestors_without_additions(mock_host):
    host = Host(name='testhost')
    group1 = Group(name='group1')
    host.groups = [group1]

    # Call populate_ancestors without additions
    host.populate_ancestors()

    # Verify that add_group was called for the existing group
    host.add_group.assert_called_once_with(group1)
