# file: lib/ansible/inventory/group.py:161-165
# asked: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}
# gained: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}

import pytest
from ansible.inventory.group import Group

def test_host_names_initial_none():
    group = Group(name="test_group")
    group._hosts = None
    group.hosts = ["host1", "host2"]
    
    result = group.host_names
    
    assert result == {"host1", "host2"}
    assert group._hosts == {"host1", "host2"}

def test_host_names_initial_set():
    group = Group(name="test_group")
    group._hosts = {"host3"}
    group.hosts = ["host1", "host2"]
    
    result = group.host_names
    
    assert result == {"host3"}
    assert group._hosts == {"host3"}
