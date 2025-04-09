# file lib/ansible/modules/iptables.py:678-680
# lines [678, 679, 680]
# branches []

import pytest
from ansible.modules.iptables import append_rule

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock()
    module_mock.run_command = mocker.MagicMock(return_value=(0, "success", ""))
    return module_mock

@pytest.fixture
def mock_push_arguments(mocker):
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-A'])

def test_append_rule(mock_module, mock_push_arguments):
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'protocol': 'tcp', 'jump': 'ACCEPT'}
    append_rule(iptables_path, mock_module, params)
    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-A'], check_rc=True)
