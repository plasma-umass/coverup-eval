# file lib/ansible/module_utils/facts/network/linux.py:287-316
# lines [289, 290, 292, 293, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316]
# branches ['292->293', '292->316', '296->297', '296->307', '298->299', '298->305', '299->300', '299->301', '302->303', '302->304', '309->310', '309->316', '313->314', '313->316']

import pytest
import re
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/sbin/ethtool'
    return mock_module

@pytest.fixture
def mock_run_command(mocker, mock_module):
    def run_command_side_effect(*args, **kwargs):
        if args[0][1] == '-k':
            return (0, "feature1: on\nfeature2: off\n", "")
        elif args[0][1] == '-T':
            return (0, "SOF_TIMESTAMPING_TX_HARDWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 42\n", "")
        else:
            return (1, "", "An error occurred")
    mock_module.run_command.side_effect = run_command_side_effect
    return mock_module.run_command

def test_get_ethtool_data(mock_module, mock_run_command):
    linux_network = LinuxNetwork(module=mock_module)
    device = 'eth0'
    data = linux_network.get_ethtool_data(device)
    
    assert data['features']['feature1'] == 'on'
    assert data['features']['feature2'] == 'off'
    assert 'tx_hardware' in data['timestamping']
    assert 'none' in data['hw_timestamp_filters']
    assert data['phc_index'] == 42
