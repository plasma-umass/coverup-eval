# file lib/ansible/playbook/role/metadata.py:112-119
# lines [112, 119]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the RoleMetadata class is imported from ansible.playbook.role.metadata
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_load_galaxy_info(role_metadata):
    attr = 'galaxy_info'
    ds = {'some_key': 'some_value'}
    
    result = role_metadata._load_galaxy_info(attr, ds)
    
    assert result == ds
