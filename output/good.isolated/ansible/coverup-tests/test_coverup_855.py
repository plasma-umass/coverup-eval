# file lib/ansible/playbook/role/metadata.py:112-119
# lines [112, 119]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Assuming the RoleMetadata class has other attributes and methods that are not shown here
# and that the Base and CollectionSearch classes are part of the ansible package.

class TestRoleMetadata:

    @pytest.fixture
    def role_metadata(self):
        return RoleMetadata()

    def test_load_galaxy_info(self, role_metadata):
        # Setup
        test_data_structure = {'some_key': 'some_value'}

        # Exercise
        galaxy_info = role_metadata._load_galaxy_info('galaxy_info', test_data_structure)

        # Verify
        assert galaxy_info == test_data_structure

        # Cleanup - nothing to do since there's no persistent state change
