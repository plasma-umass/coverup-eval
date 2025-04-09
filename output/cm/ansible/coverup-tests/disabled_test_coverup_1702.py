# file lib/ansible/playbook/role/metadata.py:47-49
# lines [48, 49]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Assuming the existence of a test file test_role_metadata.py

# New test function to cover lines 48-49
def test_role_metadata_initialization():
    # Mock owner object
    mock_owner = object()

    # Create an instance of RoleMetadata with the mock owner
    role_metadata = RoleMetadata(owner=mock_owner)

    # Assertions to verify postconditions
    assert role_metadata._owner is mock_owner

    # No cleanup necessary as no external resources are being modified
