# file: lib/ansible/playbook/role/metadata.py:127-129
# asked: {"lines": [127, 128, 129], "branches": []}
# gained: {"lines": [127, 128, 129], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    return RoleMetadata()

def test_deserialize_with_allow_duplicates(role_metadata):
    data = {'allow_duplicates': True, 'dependencies': ['dep1', 'dep2']}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is True
    assert role_metadata.dependencies == ['dep1', 'dep2']

def test_deserialize_without_allow_duplicates(role_metadata):
    data = {'dependencies': ['dep1', 'dep2']}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is False
    assert role_metadata.dependencies == ['dep1', 'dep2']

def test_deserialize_with_empty_dependencies(role_metadata):
    data = {'allow_duplicates': True}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is True
    assert role_metadata.dependencies == []

def test_deserialize_with_no_data(role_metadata):
    data = {}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is False
    assert role_metadata.dependencies == []
