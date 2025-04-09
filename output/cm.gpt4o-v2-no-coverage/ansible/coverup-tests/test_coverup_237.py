# file: lib/ansible/vars/hostvars.py:131-154
# asked: {"lines": [131, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 149, 150, 152, 153, 154], "branches": [[146, 0], [146, 147]]}
# gained: {"lines": [131, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 149, 150, 152, 153, 154], "branches": [[146, 147]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.common._collections_compat import Mapping
from ansible.template import Templar
from ansible.vars.hostvars import HostVarsVars

STATIC_VARS = ['ansible_version', 'ansible_play_hosts', 'ansible_dependent_role_names', 'ansible_play_role_names', 'ansible_role_names', 'inventory_hostname', 'inventory_hostname_short', 'inventory_file', 'inventory_dir', 'groups', 'group_names', 'omit', 'playbook_dir', 'play_hosts', 'role_names', 'ungrouped']

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_vars():
    return {
        'var1': 'value1',
        'var2': 'value2'
    }

@pytest.fixture
def host_vars(mock_vars, mock_loader):
    return HostVarsVars(mock_vars, mock_loader)

def test_getitem(host_vars, mock_vars, mock_loader):
    with patch.object(Templar, 'template', return_value='templated_value') as mock_template:
        result = host_vars['var1']
        mock_template.assert_called_once_with(mock_vars['var1'], fail_on_undefined=False, static_vars=STATIC_VARS)
        assert result == 'templated_value'

def test_contains(host_vars):
    assert 'var1' in host_vars
    assert 'var3' not in host_vars

def test_iter(host_vars):
    vars_iter = iter(host_vars)
    assert next(vars_iter) == 'var1'
    assert next(vars_iter) == 'var2'

def test_len(host_vars):
    assert len(host_vars) == 2

def test_repr(host_vars, mock_vars, mock_loader):
    with patch.object(Templar, 'template', return_value='templated_repr') as mock_template:
        result = repr(host_vars)
        mock_template.assert_called_once_with(mock_vars, fail_on_undefined=False, static_vars=STATIC_VARS)
        assert result == "'templated_repr'"
