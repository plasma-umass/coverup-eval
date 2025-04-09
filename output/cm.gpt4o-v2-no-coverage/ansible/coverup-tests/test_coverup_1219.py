# file: lib/ansible/playbook/role/requirement.py:48-49
# asked: {"lines": [49], "branches": []}
# gained: {"lines": [49], "branches": []}

import pytest
from ansible.playbook.role.requirement import RoleRequirement

def test_role_requirement_init():
    role_req = RoleRequirement()
    assert isinstance(role_req, RoleRequirement)
