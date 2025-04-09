# file: lib/ansible/vars/hostvars.py:92-96
# asked: {"lines": [92, 93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}
# gained: {"lines": [92, 93, 94, 95, 96], "branches": [[94, 95], [94, 96]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.hostvars import HostVars, AnsibleUndefined, HostVarsVars

@pytest.fixture
def hostvars_instance():
    inventory_mock = MagicMock()
    variable_manager_mock = MagicMock()
    loader_mock = MagicMock()
    return HostVars(inventory=inventory_mock, variable_manager=variable_manager_mock, loader=loader_mock)

def test_getitem_with_ansible_undefined(hostvars_instance):
    host_name = 'test_host'
    ansible_undefined_instance = AnsibleUndefined()
    
    with patch.object(hostvars_instance, 'raw_get', return_value=ansible_undefined_instance):
        result = hostvars_instance[host_name]
        assert result is ansible_undefined_instance

def test_getitem_with_valid_data(hostvars_instance):
    host_name = 'test_host'
    valid_data = {'key': 'value'}
    
    with patch.object(hostvars_instance, 'raw_get', return_value=valid_data):
        with patch('ansible.vars.hostvars.HostVarsVars', autospec=True) as HostVarsVarsMock:
            result = hostvars_instance[host_name]
            HostVarsVarsMock.assert_called_once_with(valid_data, loader=hostvars_instance._loader)
            assert result == HostVarsVarsMock.return_value
