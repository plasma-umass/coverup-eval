# file: lib/ansible/inventory/host.py:150-151
# asked: {"lines": [151], "branches": []}
# gained: {"lines": [151], "branches": []}

import pytest
from ansible.inventory.host import Host

def test_get_groups():
    host = Host()
    assert host.get_groups() == []

    group = "group1"
    host.groups.append(group)
    assert host.get_groups() == [group]

    host.groups.remove(group)
    assert host.get_groups() == []
