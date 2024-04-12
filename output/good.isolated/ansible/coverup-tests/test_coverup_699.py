# file lib/ansible/modules/iptables.py:714-717
# lines [714, 715, 716, 717]
# branches []

import pytest
from ansible.modules.iptables import get_iptables_version

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock()
    module_mock.run_command.return_value = (0, 'iptables v1.8.4\n', '')
    return module_mock

def test_get_iptables_version(mocker, mock_module):
    iptables_path = '/usr/sbin/iptables'
    mocker.patch('ansible.modules.iptables.get_iptables_version')
    version = get_iptables_version(iptables_path, mock_module)
    assert version == '1.8.4'
    mock_module.run_command.assert_called_once_with([iptables_path, '--version'], check_rc=True)
