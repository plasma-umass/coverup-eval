# file lib/ansible/playbook/role/definition.py:231-232
# lines [232]
# branches []

import pytest
from ansible.playbook.role.definition import RoleDefinition

# Assuming the RoleDefinition class has a proper __init__ method that initializes _role_params

def test_get_role_params():
    # Setup
    role_definition = RoleDefinition()
    role_definition._role_params = {'param1': 'value1', 'param2': 'value2'}

    # Exercise
    role_params_copy = role_definition.get_role_params()

    # Verify
    assert role_params_copy == role_definition._role_params
    assert role_params_copy is not role_definition._role_params  # Ensure it's a copy

    # Cleanup - nothing to do since no external resources were modified
