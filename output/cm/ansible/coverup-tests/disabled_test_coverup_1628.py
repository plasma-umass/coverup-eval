# file lib/ansible/playbook/role_include.py:179-185
# lines [180, 181, 182, 183, 184, 185]
# branches ['181->182', '181->185']

import pytest
from ansible.playbook.role_include import IncludeRole

# Mock class to simulate the parent role behavior
class MockParentRole:
    def get_role_params(self):
        return {'parent_param': 'parent_value'}

    def get_name(self):
        return 'mock_parent_role_name'

    @property
    def _role_path(self):
        return '/mock/parent/role/path'

# Test function to cover lines 180-185
@pytest.fixture
def include_role_with_parent(mocker):
    mock_role = MockParentRole()
    include_role = IncludeRole()
    mocker.patch.object(include_role, '_parent_role', new=mock_role)
    return include_role

def test_get_include_params_with_parent_role(include_role_with_parent):
    params = include_role_with_parent.get_include_params()

    assert params['parent_param'] == 'parent_value'
    assert params['ansible_parent_role_names'][0] == 'mock_parent_role_name'
    assert params['ansible_parent_role_paths'][0] == '/mock/parent/role/path'
