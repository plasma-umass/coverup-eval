# file lib/ansible/playbook/role/definition.py:234-235
# lines [234, 235]
# branches []

import pytest
from unittest.mock import patch

# Assuming the RoleDefinition class is in ansible.playbook.role.definition
from ansible.playbook.role.definition import RoleDefinition

class TestRoleDefinition:
    @pytest.fixture
    def role_definition(self):
        role_def = RoleDefinition()
        role_def._role_path = '/mock/role/path'
        yield role_def

    def test_get_role_path(self, role_definition):
        assert role_definition.get_role_path() == '/mock/role/path'
