# file lib/ansible/playbook/role/definition.py:237-240
# lines [237, 238, 239, 240]
# branches ['238->239', '238->240']

import pytest
from ansible.playbook.role.definition import RoleDefinition

# Assuming the RoleDefinition class has a constructor that accepts role and _role_collection
# If not, the test should be adjusted to match the actual constructor signature.

@pytest.fixture
def role_definition():
    # Setup
    role_def = RoleDefinition()
    role_def.role = "test_role"
    role_def._role_collection = "test_collection"
    yield role_def
    # Teardown
    # No teardown needed as we're not modifying any external state

def test_get_name_with_fqcn(role_definition):
    # Test get_name with include_role_fqcn set to True
    expected_name = "test_collection.test_role"
    assert role_definition.get_name(include_role_fqcn=True) == expected_name

def test_get_name_without_fqcn(role_definition):
    # Test get_name with include_role_fqcn set to False
    expected_name = "test_role"
    assert role_definition.get_name(include_role_fqcn=False) == expected_name

def test_get_name_with_missing_collection(role_definition):
    # Test get_name with a missing _role_collection
    role_definition._role_collection = None
    expected_name = "test_role"
    assert role_definition.get_name(include_role_fqcn=True) == expected_name

def test_get_name_with_missing_role(role_definition):
    # Test get_name with a missing role
    role_definition.role = None
    expected_name = "test_collection"
    assert role_definition.get_name(include_role_fqcn=True) == expected_name

def test_get_name_with_both_missing(role_definition):
    # Test get_name with both role and _role_collection missing
    role_definition.role = None
    role_definition._role_collection = None
    expected_name = ""
    assert role_definition.get_name(include_role_fqcn=True) == expected_name
