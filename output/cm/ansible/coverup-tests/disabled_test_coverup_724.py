# file lib/ansible/playbook/role/metadata.py:47-49
# lines [47, 48, 49]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Assuming the RoleMetadata class is part of a larger module that we're testing

class MockOwner:
    pass

@pytest.fixture
def mock_owner():
    return MockOwner()

def test_role_metadata_initialization(mock_owner):
    # Test initialization of RoleMetadata with a mock owner
    role_metadata = RoleMetadata(owner=mock_owner)
    assert role_metadata._owner is mock_owner

    # Test initialization of RoleMetadata without an owner
    role_metadata_no_owner = RoleMetadata()
    assert role_metadata_no_owner._owner is None
