# file: lib/ansible/playbook/role/definition.py:231-232
# asked: {"lines": [231, 232], "branches": []}
# gained: {"lines": [231, 232], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_get_role_params():
    role_definition = RoleDefinition()
    role_definition._role_params = {'param1': 'value1', 'param2': 'value2'}
    
    result = role_definition.get_role_params()
    
    assert result == {'param1': 'value1', 'param2': 'value2'}
    assert result is not role_definition._role_params  # Ensure a copy is returned
