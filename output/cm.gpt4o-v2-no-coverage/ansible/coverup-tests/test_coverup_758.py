# file: lib/ansible/playbook/role/metadata.py:121-125
# asked: {"lines": [121, 122, 123, 124], "branches": []}
# gained: {"lines": [121, 122, 123, 124], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_serialize(role_metadata):
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['dependency1', 'dependency2']
    
    serialized = role_metadata.serialize()
    
    assert serialized['allow_duplicates'] is True
    assert serialized['dependencies'] == ['dependency1', 'dependency2']

def test_serialize_default(role_metadata):
    role_metadata._allow_duplicates = False
    role_metadata._dependencies = []
    
    serialized = role_metadata.serialize()
    
    assert serialized['allow_duplicates'] is False
    assert serialized['dependencies'] == []
