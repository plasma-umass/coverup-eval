# file: lib/ansible/playbook/role/metadata.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

def test_role_metadata_init():
    # Test with default owner
    role_metadata = RoleMetadata()
    assert role_metadata._owner is None

    # Test with specific owner
    owner = "test_owner"
    role_metadata = RoleMetadata(owner=owner)
    assert role_metadata._owner == owner

    # Ensure that the super classes' __init__ methods are called
    assert isinstance(role_metadata, RoleMetadata)
