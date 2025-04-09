# file: lib/ansible/playbook/role/metadata.py:112-119
# asked: {"lines": [119], "branches": []}
# gained: {"lines": [119], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

class MockBase:
    pass

class MockCollectionSearch:
    pass

class MockGalaxyInfo:
    pass

class TestRoleMetadata:
    @pytest.fixture
    def role_metadata(self):
        class TestRoleMetadata(RoleMetadata, MockBase, MockCollectionSearch):
            pass
        return TestRoleMetadata()

    def test_load_galaxy_info(self, role_metadata):
        attr = 'galaxy_info'
        ds = MockGalaxyInfo()
        
        result = role_metadata._load_galaxy_info(attr, ds)
        
        assert result == ds
