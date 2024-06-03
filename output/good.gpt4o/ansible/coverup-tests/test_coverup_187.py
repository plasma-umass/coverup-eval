# file lib/ansible/vars/hostvars.py:131-154
# lines [131, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 149, 150, 152, 153, 154]
# branches ['146->exit', '146->147']

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVarsVars
from ansible.template import Templar

@pytest.fixture
def mock_templar(mocker):
    mock_templar = mocker.patch('ansible.vars.hostvars.Templar')
    instance = mock_templar.return_value
    instance.template.side_effect = lambda x, fail_on_undefined, static_vars: x
    return mock_templar

def test_hostvarsvars_getitem(mock_templar):
    variables = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(variables, loader)
    
    assert host_vars['var1'] == 'value1'
    assert host_vars['var2'] == 'value2'
    mock_templar.assert_called()

def test_hostvarsvars_contains():
    variables = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(variables, loader)
    
    assert 'var1' in host_vars
    assert 'var3' not in host_vars

def test_hostvarsvars_iter():
    variables = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(variables, loader)
    
    vars_list = list(iter(host_vars))
    assert vars_list == ['var1', 'var2']

def test_hostvarsvars_len():
    variables = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(variables, loader)
    
    assert len(host_vars) == 2

def test_hostvarsvars_repr(mock_templar):
    variables = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    host_vars = HostVarsVars(variables, loader)
    
    expected_repr = repr(variables)
    assert repr(host_vars) == expected_repr
    mock_templar.assert_called()
