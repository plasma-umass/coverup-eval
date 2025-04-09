# file lib/ansible/modules/iptables.py:698-701
# lines [699, 700, 701]
# branches []

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_module():
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(return_value=(0, "", ""))
    return module_mock

def test_set_chain_policy(mock_module):
    with patch('ansible.modules.iptables.push_arguments') as mock_push_arguments:
        mock_push_arguments.return_value = ['iptables', '-P']
        from ansible.modules.iptables import set_chain_policy
        iptables_path = 'iptables'
        params = {'policy': 'ACCEPT'}
        set_chain_policy(iptables_path, mock_module, params)
        mock_push_arguments.assert_called_once_with(iptables_path, '-P', params, make_rule=False)
        mock_module.run_command.assert_called_once_with(['iptables', '-P', 'ACCEPT'], check_rc=True)
