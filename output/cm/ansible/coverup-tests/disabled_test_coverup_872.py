# file lib/ansible/playbook/role_include.py:68-70
# lines [68, 70]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole

# Assuming the existence of the IncludeRole class as provided in the snippet.

@pytest.fixture
def include_role():
    # Setup code to create an instance of IncludeRole
    role_include = IncludeRole()
    role_include.action = 'test_action'
    role_include._role_name = 'test_role'
    yield role_include
    # No teardown needed as we're not modifying external state

def test_get_name_with_name_set(include_role):
    # Test the get_name method when the name is set
    include_role.name = 'test_name'
    assert include_role.get_name() == 'test_name'

def test_get_name_without_name_set(include_role):
    # Test the get_name method when the name is not set
    include_role.name = None
    expected_name = 'test_action : test_role'
    assert include_role.get_name() == expected_name
