# file lib/ansible/playbook/role/metadata.py:121-125
# lines [121, 122, 123, 124]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

# Assuming the RoleMetadata class has the following __init__ method for this example
# (since it's not provided in the question, I'm creating a mock one):
# def __init__(self):
#     self._allow_duplicates = None
#     self._dependencies = None

@pytest.fixture
def role_metadata(mocker):
    # Setup phase: create a RoleMetadata instance with test values
    mocker.patch.object(RoleMetadata, '__init__', return_value=None)
    metadata = RoleMetadata()
    metadata._allow_duplicates = True
    metadata._dependencies = ['role1', 'role2']
    yield metadata
    # Teardown phase: nothing to do here for this simple test case

def test_role_metadata_serialize(role_metadata):
    # Act: Serialize the role metadata
    serialized_data = role_metadata.serialize()

    # Assert: Check if the serialized data matches the expected result
    assert serialized_data == {
        'allow_duplicates': True,
        'dependencies': ['role1', 'role2']
    }
