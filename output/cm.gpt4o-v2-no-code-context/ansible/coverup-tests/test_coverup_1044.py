# file: lib/ansible/playbook/role/metadata.py:121-125
# asked: {"lines": [122, 123, 124], "branches": []}
# gained: {"lines": [122, 123, 124], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    class MockBase:
        pass

    class MockCollectionSearch:
        pass

    class TestRoleMetadata(RoleMetadata, MockBase, MockCollectionSearch):
        def __init__(self, allow_duplicates, dependencies):
            self._allow_duplicates = allow_duplicates
            self._dependencies = dependencies

    return TestRoleMetadata

def test_serialize(role_metadata):
    role = role_metadata(allow_duplicates=True, dependencies=['dep1', 'dep2'])
    serialized = role.serialize()
    
    assert serialized['allow_duplicates'] == True
    assert serialized['dependencies'] == ['dep1', 'dep2']
