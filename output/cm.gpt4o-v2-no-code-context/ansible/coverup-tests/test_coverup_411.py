# file: lib/ansible/playbook/role_include.py:179-185
# asked: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}
# gained: {"lines": [179, 180, 181, 182, 183, 184, 185], "branches": [[181, 182], [181, 185]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.role_include import IncludeRole, TaskInclude

class TestIncludeRole:
    @pytest.fixture
    def include_role(self):
        parent_role_mock = Mock()
        parent_role_mock.get_role_params.return_value = {'param1': 'value1'}
        parent_role_mock.get_name.return_value = 'parent_role_name'
        parent_role_mock._role_path = '/path/to/parent_role'

        include_role = IncludeRole()
        include_role._parent_role = parent_role_mock
        return include_role

    def test_get_include_params_with_parent_role(self, include_role):
        result = include_role.get_include_params()

        assert 'param1' in result
        assert result['param1'] == 'value1'
        assert 'ansible_parent_role_names' in result
        assert result['ansible_parent_role_names'][0] == 'parent_role_name'
        assert 'ansible_parent_role_paths' in result
        assert result['ansible_parent_role_paths'][0] == '/path/to/parent_role'

    def test_get_include_params_without_parent_role(self):
        include_role = IncludeRole()
        include_role._parent_role = None

        result = include_role.get_include_params()

        assert 'param1' not in result
        assert 'ansible_parent_role_names' not in result
        assert 'ansible_parent_role_paths' not in result
