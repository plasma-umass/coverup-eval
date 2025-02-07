# file: lib/ansible/inventory/host.py:150-151
# asked: {"lines": [150, 151], "branches": []}
# gained: {"lines": [150, 151], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="testhost")

def test_get_groups(host):
    # Ensure the groups list is initially empty
    assert host.get_groups() == []

    # Add a group and test again
    host.groups.append("group1")
    assert host.get_groups() == ["group1"]

    # Clean up
    host.groups.clear()
    assert host.get_groups() == []
