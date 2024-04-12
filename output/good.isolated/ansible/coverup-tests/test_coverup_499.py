# file lib/ansible/playbook/role_include.py:179-185
# lines [179, 180, 181, 182, 183, 184, 185]
# branches ['181->182', '181->185']

import pytest
from ansible.playbook.role_include import IncludeRole

# Mock class to simulate the parent role behavior
class MockParentRole:
    def __init__(self, name, role_path):
        self._name = name
        self._role_path = role_path

    def get_role_params(self):
        return {'some_param': 'some_value'}

    def get_name(self):
        return self._name

@pytest.fixture
def mock_parent_role():
    # Setup the mock parent role with a name and a role path
    return MockParentRole(name='parent_role', role_path='/path/to/parent_role')

def test_get_include_params_with_parent_role(mock_parent_role):
    # Create an instance of IncludeRole with a mock parent role
    include_role = IncludeRole()
    include_role._parent_role = mock_parent_role

    # Call the method under test
    params = include_role.get_include_params()

    # Assertions to verify the postconditions
    assert 'some_param' in params
    assert params['some_param'] == 'some_value'
    assert 'ansible_parent_role_names' in params
    assert params['ansible_parent_role_names'][0] == 'parent_role'
    assert 'ansible_parent_role_paths' in params
    assert params['ansible_parent_role_paths'][0] == '/path/to/parent_role'
