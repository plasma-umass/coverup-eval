# file: lib/ansible/playbook/role_include.py:179-185
# asked: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}
# gained: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}

import pytest
from ansible.playbook.role_include import IncludeRole
from unittest.mock import MagicMock

@pytest.fixture
def include_role():
    role = MagicMock()
    role.get_role_params.return_value = {'param1': 'value1'}
    role.get_name.return_value = 'test_role'
    role._role_path = '/path/to/role'
    return IncludeRole(role=role)

def test_get_include_params_with_parent_role(include_role):
    params = include_role.get_include_params()
    assert params['param1'] == 'value1'
    assert params['ansible_parent_role_names'] == ['test_role']
    assert params['ansible_parent_role_paths'] == ['/path/to/role']

def test_get_include_params_without_parent_role():
    include_role = IncludeRole(role=None)
    params = include_role.get_include_params()
    assert 'ansible_parent_role_names' not in params
    assert 'ansible_parent_role_paths' not in params
