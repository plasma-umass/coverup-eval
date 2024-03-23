# file lib/ansible/playbook/role/definition.py:231-232
# lines [231, 232]
# branches []

import pytest
from ansible.playbook.role.definition import RoleDefinition

# Assuming the RoleDefinition class has the necessary __init__ method and other dependencies

@pytest.fixture
def role_definition():
    # Setup for the test with necessary mock objects if required
    role_def = RoleDefinition()
    role_def._role_params = {'param1': 'value1', 'param2': 'value2'}
    yield role_def
    # Teardown after the test
    # No specific teardown required in this case

def test_get_role_params(role_definition):
    # Call the method we want to test
    role_params = role_definition.get_role_params()

    # Check that the method returns a copy, not the original dict
    assert role_params is not role_definition._role_params
    assert role_params == role_definition._role_params

    # Modify the copy and ensure the original is not affected
    role_params['param1'] = 'new_value'
    assert role_definition._role_params['param1'] == 'value1'
