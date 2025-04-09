# file: lib/ansible/playbook/role/metadata.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.playbook.base import Base
from ansible.playbook.collectionsearch import CollectionSearch

def test_role_metadata_init():
    # Test initialization without owner
    role_metadata = RoleMetadata()
    assert role_metadata._owner is None

    # Test initialization with owner
    owner = "test_owner"
    role_metadata = RoleMetadata(owner=owner)
    assert role_metadata._owner == owner

def test_role_metadata_inheritance():
    # Ensure RoleMetadata inherits from Base and CollectionSearch
    role_metadata = RoleMetadata()
    assert isinstance(role_metadata, Base)
    assert isinstance(role_metadata, CollectionSearch)
