# file: lib/ansible/inventory/host.py:115-126
# asked: {"lines": [], "branches": [[119, 118]]}
# gained: {"lines": [], "branches": [[119, 118]]}

import pytest
from unittest.mock import Mock

class TestHost:
    @pytest.fixture
    def host(self):
        from ansible.inventory.host import Host
        return Host()

    def test_add_group_with_new_ancestor(self, host):
        group = Mock()
        ancestor_group = Mock()
        group.get_ancestors.return_value = [ancestor_group]
        
        # Ensure the ancestor group is not in host.groups initially
        assert ancestor_group not in host.groups
        
        added = host.add_group(group)
        
        # Verify the ancestor group was added
        assert ancestor_group in host.groups
        # Verify the group itself was added
        assert group in host.groups
        # Verify the method returned True
        assert added

    def test_add_group_with_existing_ancestor(self, host):
        group = Mock()
        ancestor_group = Mock()
        group.get_ancestors.return_value = [ancestor_group]
        
        # Add the ancestor group initially
        host.groups.append(ancestor_group)
        
        added = host.add_group(group)
        
        # Verify the ancestor group is still in host.groups
        assert ancestor_group in host.groups
        # Verify the group itself was added
        assert group in host.groups
        # Verify the method returned True
        assert added

    def test_add_group_without_ancestors(self, host):
        group = Mock()
        group.get_ancestors.return_value = []
        
        # Ensure the group is not in host.groups initially
        assert group not in host.groups
        
        added = host.add_group(group)
        
        # Verify the group itself was added
        assert group in host.groups
        # Verify the method returned True
        assert added

    def test_add_existing_group(self, host):
        group = Mock()
        group.get_ancestors.return_value = []
        
        # Add the group initially
        host.groups.append(group)
        
        added = host.add_group(group)
        
        # Verify the group is still in host.groups
        assert group in host.groups
        # Verify the method returned False since the group was already present
        assert not added
