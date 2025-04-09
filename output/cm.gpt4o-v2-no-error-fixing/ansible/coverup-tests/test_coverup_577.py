# file: lib/ansible/playbook/role/definition.py:234-235
# asked: {"lines": [234, 235], "branches": []}
# gained: {"lines": [234, 235], "branches": []}

import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_get_role_path():
    role_definition = RoleDefinition()
    role_definition._role_path = "/path/to/role"
    assert role_definition.get_role_path() == "/path/to/role"
