# file: lib/ansible/inventory/host.py:115-126
# asked: {"lines": [115, 116, 118, 119, 120, 123, 124, 125, 126], "branches": [[118, 119], [118, 123], [119, 118], [119, 120], [123, 124], [123, 126]]}
# gained: {"lines": [115, 116, 118, 119, 120, 123, 124, 125, 126], "branches": [[118, 119], [118, 123], [119, 118], [119, 120], [123, 124], [123, 126]]}

import pytest
from unittest.mock import Mock

from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host()

def test_add_group_new_group(host):
    group = Mock()
    group.get_ancestors.return_value = []

    added = host.add_group(group)

    assert added is True
    assert group in host.groups

def test_add_group_existing_group(host):
    group = Mock()
    group.get_ancestors.return_value = []
    host.groups.append(group)

    added = host.add_group(group)

    assert added is False
    assert host.groups.count(group) == 1

def test_add_group_with_ancestors(host):
    ancestor = Mock()
    group = Mock()
    group.get_ancestors.return_value = [ancestor]

    added = host.add_group(group)

    assert added is True
    assert ancestor in host.groups
    assert group in host.groups

def test_add_group_with_existing_ancestors(host, monkeypatch):
    ancestor = Mock()
    group = Mock()
    group.get_ancestors.return_value = [ancestor]
    host.groups.append(ancestor)

    added = host.add_group(group)

    assert added is True
    assert host.groups.count(ancestor) == 1
    assert group in host.groups
