# file: lib/ansible/playbook/role/definition.py:237-240
# asked: {"lines": [237, 238, 239, 240], "branches": [[238, 239], [238, 240]]}
# gained: {"lines": [237, 238, 239, 240], "branches": [[238, 239], [238, 240]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition

class MockRoleDefinition(RoleDefinition):
    def __init__(self, role_collection, role):
        self._role_collection = role_collection
        self.role = role

@pytest.fixture
def role_definition():
    return MockRoleDefinition(role_collection="collection_name", role="role_name")

def test_get_name_with_fqcn(role_definition):
    result = role_definition.get_name(include_role_fqcn=True)
    assert result == "collection_name.role_name"

def test_get_name_without_fqcn(role_definition):
    result = role_definition.get_name(include_role_fqcn=False)
    assert result == "role_name"
