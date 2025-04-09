# file: lib/ansible/playbook/role/metadata.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

def test_role_metadata_init_with_owner():
    owner = "test_owner"
    role_metadata = RoleMetadata(owner=owner)
    assert role_metadata._owner == owner

def test_role_metadata_init_without_owner():
    role_metadata = RoleMetadata()
    assert role_metadata._owner is None
