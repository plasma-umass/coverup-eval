# file: lib/ansible/playbook/role/metadata.py:112-119
# asked: {"lines": [112, 119], "branches": []}
# gained: {"lines": [112, 119], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

class TestRoleMetadata:
    def test_load_galaxy_info(self):
        role_metadata = RoleMetadata()
        attr = 'galaxy_info'
        ds = {'name': 'example_role', 'version': '1.0.0'}
        
        result = role_metadata._load_galaxy_info(attr, ds)
        
        assert result == ds
