# file lib/ansible/playbook/role/metadata.py:112-119
# lines [119]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    # Setup for the RoleMetadata object
    metadata = RoleMetadata()
    yield metadata
    # Teardown for the RoleMetadata object, if necessary

def test_load_galaxy_info(role_metadata):
    # Define a sample data structure that would represent the 'ds' argument
    sample_ds = {'name': 'test_role', 'author': 'test_author'}

    # Call the _load_galaxy_info method with the sample data
    result = role_metadata._load_galaxy_info('galaxy_info', sample_ds)

    # Assert that the result is the same as the input data structure
    assert result == sample_ds, "The _load_galaxy_info method should return the input data structure unchanged"
