# file: lib/ansible/vars/hostvars.py:131-154
# asked: {"lines": [], "branches": [[146, 0]]}
# gained: {"lines": [], "branches": [[146, 0]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.common._collections_compat import Mapping
from ansible.template import Templar
from ansible.vars.hostvars import HostVarsVars

STATIC_VARS = ['ansible_version', 'ansible_play_hosts', 'ansible_dependent_role_names', 'ansible_play_role_names', 'ansible_role_names', 'inventory_hostname', 'inventory_hostname_short', 'inventory_file', 'inventory_dir', 'groups', 'group_names', 'omit', 'playbook_dir', 'play_hosts', 'role_names', 'ungrouped']

class TestHostVarsVars:

    @pytest.fixture
    def mock_loader(self):
        return MagicMock()

    @pytest.fixture
    def host_vars(self, mock_loader):
        variables = {
            'var1': 'value1',
            'var2': 'value2'
        }
        return HostVarsVars(variables, mock_loader)

    @patch('ansible.template.Templar.template')
    def test_getitem(self, mock_template, host_vars):
        mock_template.return_value = 'templated_value'
        assert host_vars['var1'] == 'templated_value'
        mock_template.assert_called_once()
        args, kwargs = mock_template.call_args
        assert args == ('value1',)
        assert kwargs['fail_on_undefined'] == False
        assert kwargs['static_vars'] == STATIC_VARS

    def test_contains(self, host_vars):
        assert 'var1' in host_vars
        assert 'var3' not in host_vars

    def test_iter(self, host_vars):
        vars_iter = iter(host_vars)
        assert next(vars_iter) == 'var1'
        assert next(vars_iter) == 'var2'
        with pytest.raises(StopIteration):
            next(vars_iter)

    def test_len(self, host_vars):
        assert len(host_vars) == 2

    @patch('ansible.template.Templar.template')
    def test_repr(self, mock_template, host_vars):
        mock_template.return_value = {'var1': 'templated_value1', 'var2': 'templated_value2'}
        assert repr(host_vars) == "{'var1': 'templated_value1', 'var2': 'templated_value2'}"
        mock_template.assert_called_once()
        args, kwargs = mock_template.call_args
        assert args == (host_vars._vars,)
        assert kwargs['fail_on_undefined'] == False
        assert kwargs['static_vars'] == STATIC_VARS
