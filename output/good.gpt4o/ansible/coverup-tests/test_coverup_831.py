# file lib/ansible/playbook/role/definition.py:231-232
# lines [231, 232]
# branches []

import pytest
from ansible.playbook.role.definition import RoleDefinition

class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestRoleDefinition(RoleDefinition, MockBase, MockConditional, MockTaggable, MockCollectionSearch):
    def __init__(self, role_params):
        self._role_params = role_params

def test_get_role_params():
    role_params = {'param1': 'value1', 'param2': 'value2'}
    role_def = TestRoleDefinition(role_params)
    
    result = role_def.get_role_params()
    
    assert result == role_params
    assert result is not role_params  # Ensure a copy is returned
