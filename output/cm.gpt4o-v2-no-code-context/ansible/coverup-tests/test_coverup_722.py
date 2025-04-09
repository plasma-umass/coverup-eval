# file: lib/ansible/playbook/role/definition.py:231-232
# asked: {"lines": [231, 232], "branches": []}
# gained: {"lines": [231, 232], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    class MockRoleDefinition(RoleDefinition):
        def __init__(self):
            self._role_params = {'param1': 'value1', 'param2': 'value2'}
    
    return MockRoleDefinition()

def test_get_role_params(role_definition):
    role_params = role_definition.get_role_params()
    assert role_params == {'param1': 'value1', 'param2': 'value2'}
    assert role_params is not role_definition._role_params  # Ensure it's a copy, not the same object
