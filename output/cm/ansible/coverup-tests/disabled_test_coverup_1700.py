# file lib/ansible/playbook/role/metadata.py:127-129
# lines [128, 129]
# branches []

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_role_metadata_deserialize_allow_duplicates_and_dependencies(role_metadata):
    test_data = {
        'allow_duplicates': True,
        'dependencies': ['dependency1', 'dependency2']
    }
    role_metadata.deserialize(test_data)
    assert getattr(role_metadata, 'allow_duplicates') == True
    assert getattr(role_metadata, 'dependencies') == ['dependency1', 'dependency2']

def test_role_metadata_deserialize_default_allow_duplicates_and_dependencies(role_metadata):
    test_data = {}
    role_metadata.deserialize(test_data)
    assert getattr(role_metadata, 'allow_duplicates') == False
    assert getattr(role_metadata, 'dependencies') == []
