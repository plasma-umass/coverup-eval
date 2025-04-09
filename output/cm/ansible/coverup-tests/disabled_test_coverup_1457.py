# file lib/ansible/playbook/role/metadata.py:112-119
# lines [119]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Assuming the RoleMetadata class has other necessary methods and attributes
# and that the _load_galaxy_info method is part of a larger class definition.

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_load_galaxy_info(role_metadata):
    test_data_structure = {'some_key': 'some_value'}
    result = role_metadata._load_galaxy_info('galaxy_info', test_data_structure)
    assert result == test_data_structure, "The _load_galaxy_info method should return the provided data structure unchanged."
