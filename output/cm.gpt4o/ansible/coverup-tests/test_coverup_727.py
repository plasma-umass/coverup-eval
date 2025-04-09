# file lib/ansible/modules/iptables.py:693-695
# lines [693, 694, 695]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule

# Assuming push_arguments is defined somewhere in the module
from ansible.modules.iptables import flush_table

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    module.run_command = mocker.Mock()
    return module

def test_flush_table(mocker, mock_module):
    iptables_path = '/sbin/iptables'
    params = {'table': 'filter'}

    # Mock push_arguments to return a specific command
    mock_push_arguments = mocker.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-F'])

    flush_table(iptables_path, mock_module, params)

    # Verify that push_arguments was called with the correct parameters
    mock_push_arguments.assert_called_once_with(iptables_path, '-F', params, make_rule=False)

    # Verify that run_command was called with the correct command
    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-F'], check_rc=True)
