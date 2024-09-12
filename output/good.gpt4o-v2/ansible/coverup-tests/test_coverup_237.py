# file: lib/ansible/inventory/host.py:115-126
# asked: {"lines": [115, 116, 118, 119, 120, 123, 124, 125, 126], "branches": [[118, 119], [118, 123], [119, 118], [119, 120], [123, 124], [123, 126]]}
# gained: {"lines": [115, 116, 118, 119, 120, 123, 124, 125, 126], "branches": [[118, 119], [118, 123], [119, 120], [123, 124], [123, 126]]}

import pytest
from unittest.mock import Mock

from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

def test_add_group_with_ancestors(host):
    group = Mock()
    ancestor_group = Mock()
    group.get_ancestors.return_value = [ancestor_group]
    
    assert ancestor_group not in host.groups
    assert group not in host.groups
    
    added = host.add_group(group)
    
    assert ancestor_group in host.groups
    assert group in host.groups
    assert added

def test_add_group_without_ancestors(host):
    group = Mock()
    group.get_ancestors.return_value = []
    
    assert group not in host.groups
    
    added = host.add_group(group)
    
    assert group in host.groups
    assert added

def test_add_existing_group(host):
    group = Mock()
    group.get_ancestors.return_value = []
    
    host.groups.append(group)
    
    added = host.add_group(group)
    
    assert host.groups.count(group) == 1
    assert not added
