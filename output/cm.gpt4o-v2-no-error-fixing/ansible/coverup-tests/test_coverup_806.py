# file: lib/ansible/playbook/role/metadata.py:121-125
# asked: {"lines": [122, 123, 124], "branches": []}
# gained: {"lines": [122, 123, 124], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_serialize(role_metadata):
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['dependency1', 'dependency2']
    
    serialized_data = role_metadata.serialize()
    
    assert serialized_data['allow_duplicates'] == True
    assert serialized_data['dependencies'] == ['dependency1', 'dependency2']
