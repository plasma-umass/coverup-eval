# file lib/ansible/inventory/group.py:234-242
# lines [234, 235, 236, 237, 238, 239, 240, 241, 242]
# branches ['236->237', '236->242']

import pytest
from ansible.inventory.group import Group
from ansible.inventory.host import Host

@pytest.fixture
def group_and_host():
    # Setup
    group = Group('test_group')
    host = Host('test_host')
    group.add_host(host)

    # Yield for the test
    yield group, host

    # Cleanup
    group.remove_host(host)

def test_remove_host(group_and_host):
    group, host = group_and_host

    # Pre-conditions
    assert host.name in group.host_names
    assert host in group.hosts

    # Test remove_host
    removed = group.remove_host(host)

    # Post-conditions
    assert removed is True
    assert host.name not in group.host_names
    assert host not in group.hosts
    assert group not in host.groups

def test_remove_nonexistent_host(group_and_host):
    group, _ = group_and_host
    non_existent_host = Host('non_existent_host')

    # Pre-conditions
    assert non_existent_host.name not in group.host_names

    # Test remove_host with a host that is not in the group
    removed = group.remove_host(non_existent_host)

    # Post-conditions
    assert removed is False
