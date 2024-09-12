# file: lib/ansible/inventory/group.py:234-242
# asked: {"lines": [237, 238, 239, 240, 241], "branches": [[236, 237]]}
# gained: {"lines": [237, 238, 239, 240, 241], "branches": [[236, 237]]}

import pytest
from ansible.inventory.group import Group

class MockHost:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def remove_group(self, group):
        self.groups.remove(group)

@pytest.fixture
def group():
    grp = Group(name="test_group")
    return grp

@pytest.fixture
def host():
    return MockHost(name="test_host")

def test_remove_host(group, host, mocker):
    # Add host to group
    group.hosts.append(host)
    group._hosts = [host.name]
    host.groups.append(group)

    # Mock the host_names property to include the host name
    mocker.patch.object(group.__class__, 'host_names', new_callable=mocker.PropertyMock, return_value=[host.name])

    # Remove the host
    removed = group.remove_host(host)

    # Assertions to verify postconditions
    assert removed is True
    assert host not in group.hosts
    assert host.name not in group._hosts
    assert group not in host.groups

    # Clean up
    group.hosts = []
    group._hosts = []
    host.groups = []
