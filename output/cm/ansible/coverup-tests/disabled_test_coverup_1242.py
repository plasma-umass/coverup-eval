# file lib/ansible/playbook/role/definition.py:205-229
# lines [211, 212, 213, 214, 222, 224, 227, 229]
# branches ['214->222', '214->229', '222->224', '222->227']

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.utils.sentinel import Sentinel
from ansible.module_utils.six import iteritems

# Mocking the RoleDefinition class to add _valid_attrs
class MockRoleDefinition(RoleDefinition):
    _valid_attrs = {
        'name': Sentinel,
        'vars': Sentinel,
        # 'tasks' is removed from the valid attributes to trigger the missing lines
    }

@pytest.fixture
def role_definition():
    return MockRoleDefinition()

def test_split_role_params(role_definition):
    test_data = {
        'name': 'test_role',
        'vars': {'var1': 'value1'},
        'tasks': [{'debug': {'msg': 'Hello world'}}],  # This should now be treated as an extra param
        'extra_param1': 'extra_value1',
        'extra_param2': 'extra_value2',
    }
    role_def, role_params = role_definition._split_role_params(test_data)
    
    # Assertions to check if the role definition and params are split correctly
    assert role_def == {
        'name': 'test_role',
        'vars': {'var1': 'value1'},
    }
    assert role_params == {
        'tasks': [{'debug': {'msg': 'Hello world'}}],  # 'tasks' should now be in role_params
        'extra_param1': 'extra_value1',
        'extra_param2': 'extra_value2',
    }
