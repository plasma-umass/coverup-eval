# file lib/ansible/playbook/role/metadata.py:47-49
# lines [47, 48, 49]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

def test_role_metadata_initialization():
    owner = "test_owner"
    role_metadata = RoleMetadata(owner=owner)
    
    assert role_metadata._owner == owner

def test_role_metadata_no_owner():
    role_metadata = RoleMetadata()
    
    assert role_metadata._owner is None
