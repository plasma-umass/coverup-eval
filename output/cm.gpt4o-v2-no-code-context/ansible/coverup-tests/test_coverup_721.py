# file: lib/ansible/playbook/role/definition.py:234-235
# asked: {"lines": [234, 235], "branches": []}
# gained: {"lines": [234, 235], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    class MockRoleDefinition(RoleDefinition):
        def __init__(self, role_path):
            self._role_path = role_path

    return MockRoleDefinition

def test_get_role_path(role_definition):
    role_path = "/path/to/role"
    role_def = role_definition(role_path)
    assert role_def.get_role_path() == role_path
