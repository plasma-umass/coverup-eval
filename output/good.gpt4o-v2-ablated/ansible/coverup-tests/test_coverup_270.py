# file: lib/ansible/playbook/role/metadata.py:121-125
# asked: {"lines": [121, 122, 123, 124], "branches": []}
# gained: {"lines": [121, 122, 123, 124], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

class MockBase:
    pass

class MockCollectionSearch:
    pass

@pytest.fixture
def role_metadata(monkeypatch):
    class MockRoleMetadata(MockBase, MockCollectionSearch, RoleMetadata):
        def __init__(self):
            self._allow_duplicates = True
            self._dependencies = ['dependency1', 'dependency2']
    
    monkeypatch.setattr('ansible.playbook.role.metadata.RoleMetadata', MockRoleMetadata)
    return MockRoleMetadata()

def test_serialize(role_metadata):
    serialized_data = role_metadata.serialize()
    assert serialized_data == {
        'allow_duplicates': True,
        'dependencies': ['dependency1', 'dependency2']
    }
