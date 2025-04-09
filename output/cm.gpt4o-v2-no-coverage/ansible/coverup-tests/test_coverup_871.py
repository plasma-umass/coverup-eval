# file: lib/ansible/playbook/role/metadata.py:112-119
# asked: {"lines": [112, 119], "branches": []}
# gained: {"lines": [112, 119], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

class TestRoleMetadata:
    
    def test_load_galaxy_info(self):
        role_metadata = RoleMetadata()
        attr = "galaxy_info"
        ds = {"author": "test_author", "description": "test_description"}
        
        result = role_metadata._load_galaxy_info(attr, ds)
        
        assert result == ds
