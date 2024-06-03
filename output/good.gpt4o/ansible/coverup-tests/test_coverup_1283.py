# file lib/ansible/modules/iptables.py:688-690
# lines [689, 690]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.iptables import remove_rule

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    module.run_command = mocker.Mock(return_value=(0, '', ''))
    return module

def test_remove_rule_executes_command(mock_module, mocker):
    iptables_path = '/sbin/iptables'
    params = ['INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT']
    
    mock_push_arguments = mocker.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-D', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT'])
    
    remove_rule(iptables_path, mock_module, params)
    
    mock_push_arguments.assert_called_once_with(iptables_path, '-D', params)
    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-D', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT'], check_rc=True)
