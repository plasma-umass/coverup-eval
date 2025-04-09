# file: lib/ansible/playbook/role_include.py:179-185
# asked: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}
# gained: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}

import pytest
from ansible.playbook.role_include import IncludeRole
from unittest.mock import Mock

@pytest.fixture
def mock_parent_role():
    mock_role = Mock()
    mock_role.get_role_params.return_value = {'param1': 'value1'}
    mock_role.get_name.return_value = 'mock_role_name'
    mock_role._role_path = '/mock/role/path'
    return mock_role

def test_get_include_params_with_parent_role(mock_parent_role):
    include_role = IncludeRole()
    include_role._parent_role = mock_parent_role

    params = include_role.get_include_params()

    assert params['param1'] == 'value1'
    assert params['ansible_parent_role_names'] == ['mock_role_name']
    assert params['ansible_parent_role_paths'] == ['/mock/role/path']

def test_get_include_params_without_parent_role():
    include_role = IncludeRole()
    include_role._parent_role = None

    params = include_role.get_include_params()

    assert 'param1' not in params
    assert 'ansible_parent_role_names' not in params
    assert 'ansible_parent_role_paths' not in params
