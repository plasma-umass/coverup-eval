# file lib/ansible/playbook/role_include.py:179-185
# lines []
# branches ['181->185']

import pytest
from unittest.mock import Mock
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_task_include(mocker):
    mocker.patch('ansible.playbook.role_include.TaskInclude', autospec=True)

def test_include_role_with_parent_role(mock_task_include):
    parent_role_mock = Mock()
    parent_role_mock.get_role_params.return_value = {'param1': 'value1'}
    parent_role_mock.get_name.return_value = 'parent_role_name'
    parent_role_mock._role_path = '/path/to/parent_role'

    include_role = IncludeRole()
    include_role._parent_role = parent_role_mock

    params = include_role.get_include_params()

    assert params['param1'] == 'value1'
    assert params['ansible_parent_role_names'] == ['parent_role_name']
    assert params['ansible_parent_role_paths'] == ['/path/to/parent_role']

def test_include_role_without_parent_role(mock_task_include):
    include_role = IncludeRole()
    include_role._parent_role = None

    params = include_role.get_include_params()

    assert 'ansible_parent_role_names' not in params
    assert 'ansible_parent_role_paths' not in params
