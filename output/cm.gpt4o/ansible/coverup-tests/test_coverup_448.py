# file lib/ansible/playbook/role_include.py:179-185
# lines [179, 180, 181, 182, 183, 184, 185]
# branches ['181->182', '181->185']

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_task_include():
    with patch('ansible.playbook.role_include.TaskInclude', autospec=True) as mock:
        yield mock

def test_include_role_get_include_params(mock_task_include):
    mock_parent_role = Mock()
    mock_parent_role.get_role_params.return_value = {'param1': 'value1'}
    mock_parent_role.get_name.return_value = 'parent_role_name'
    mock_parent_role._role_path = '/path/to/parent_role'

    include_role = IncludeRole()
    include_role._parent_role = mock_parent_role

    params = include_role.get_include_params()

    assert params['param1'] == 'value1'
    assert params['ansible_parent_role_names'] == ['parent_role_name']
    assert params['ansible_parent_role_paths'] == ['/path/to/parent_role']

    mock_parent_role.get_role_params.assert_called_once()
    mock_parent_role.get_name.assert_called_once()
