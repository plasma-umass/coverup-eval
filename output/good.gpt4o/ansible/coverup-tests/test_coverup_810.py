# file lib/ansible/playbook/role/requirement.py:48-49
# lines [48, 49]
# branches []

import pytest
from ansible.playbook.role.requirement import RoleRequirement

def test_role_requirement_initialization():
    # Create an instance of RoleRequirement
    role_req = RoleRequirement()
    
    # Assert that the instance is indeed a RoleRequirement
    assert isinstance(role_req, RoleRequirement)
    
    # Assert that the instance is also a RoleDefinition (since RoleRequirement inherits from RoleDefinition)
    from ansible.playbook.role.definition import RoleDefinition
    assert isinstance(role_req, RoleDefinition)
