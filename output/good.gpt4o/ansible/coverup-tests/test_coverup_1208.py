# file lib/ansible/playbook/role/definition.py:237-240
# lines [238, 239, 240]
# branches ['238->239', '238->240']

import pytest
from unittest.mock import Mock

# Assuming the RoleDefinition class is imported from ansible.playbook.role.definition
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition():
    # Mocking the necessary attributes for RoleDefinition
    role_def = RoleDefinition()
    role_def._role_collection = 'collection_name'
    role_def.role = 'role_name'
    return role_def

def test_get_name_with_fqcn(role_definition):
    # Test when include_role_fqcn is True
    result = role_definition.get_name(include_role_fqcn=True)
    assert result == 'collection_name.role_name'

def test_get_name_without_fqcn(role_definition):
    # Test when include_role_fqcn is False
    result = role_definition.get_name(include_role_fqcn=False)
    assert result == 'role_name'
