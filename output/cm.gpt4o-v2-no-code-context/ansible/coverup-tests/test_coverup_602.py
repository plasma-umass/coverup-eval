# file: lib/ansible/playbook/role/metadata.py:121-125
# asked: {"lines": [121, 122, 123, 124], "branches": []}
# gained: {"lines": [121], "branches": []}

import pytest
from ansible.playbook.role.metadata import RoleMetadata

@pytest.fixture
def role_metadata():
    class MockBase:
        pass

    class MockCollectionSearch:
        pass

    class MockRoleMetadata(MockBase, MockCollectionSearch):
        def __init__(self, allow_duplicates, dependencies):
            self._allow_duplicates = allow_duplicates
            self._dependencies = dependencies

        def serialize(self):
            return dict(
                allow_duplicates=self._allow_duplicates,
                dependencies=self._dependencies
            )

    return MockRoleMetadata

def test_serialize_with_dependencies(role_metadata):
    role = role_metadata(allow_duplicates=True, dependencies=['dep1', 'dep2'])
    serialized = role.serialize()
    assert serialized['allow_duplicates'] is True
    assert serialized['dependencies'] == ['dep1', 'dep2']

def test_serialize_without_dependencies(role_metadata):
    role = role_metadata(allow_duplicates=False, dependencies=[])
    serialized = role.serialize()
    assert serialized['allow_duplicates'] is False
    assert serialized['dependencies'] == []
