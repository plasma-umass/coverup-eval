# file lib/ansible/modules/iptables.py:683-685
# lines [683, 684, 685]
# branches []

import pytest
from ansible.modules.iptables import insert_rule

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command.return_value = (0, "success", "")
    return mock_module

@pytest.fixture
def mock_push_arguments(mocker):
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-I'])

def test_insert_rule(mock_module, mock_push_arguments):
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'source': '127.0.0.1', 'jump': 'ACCEPT'}
    insert_rule(iptables_path, mock_module, params)
    mock_module.run_command.assert_called_once()
    args, kwargs = mock_module.run_command.call_args
    assert args[0] == ['/sbin/iptables', '-I']
    assert kwargs['check_rc'] == True
