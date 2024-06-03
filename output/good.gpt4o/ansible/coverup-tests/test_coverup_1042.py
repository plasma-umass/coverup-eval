# file lib/ansible/module_utils/facts/network/linux.py:287-316
# lines [289, 290, 292, 293, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316]
# branches ['292->293', '292->316', '296->297', '296->307', '298->299', '298->305', '299->300', '299->301', '302->303', '302->304', '309->310', '309->316', '313->314', '313->316']

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_module(mocker):
    module = Mock()
    module.get_bin_path = mocker.Mock(return_value='/usr/sbin/ethtool')
    module.run_command = mocker.Mock()
    return module

@pytest.fixture
def linux_network(mock_module):
    from ansible.module_utils.facts.network.linux import LinuxNetwork
    network = LinuxNetwork(mock_module)
    return network

def test_get_ethtool_data_features(linux_network, mock_module):
    device = 'eth0'
    mock_module.run_command.side_effect = [
        (0, 'feature1: on\nfeature2: off\n', ''),
        (0, 'SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_PTP_V2_L2_EVENT\nPTP Hardware Clock: 2\n', '')
    ]

    data = linux_network.get_ethtool_data(device)

    assert 'features' in data
    assert data['features'] == {'feature1': 'on', 'feature2': 'off'}
    assert 'timestamping' in data
    assert data['timestamping'] == ['tx_software']
    assert 'hw_timestamp_filters' in data
    assert data['hw_timestamp_filters'] == ['ptp_v2_l2_event']
    assert 'phc_index' in data
    assert data['phc_index'] == 2

def test_get_ethtool_data_no_ethtool(linux_network, mock_module):
    mock_module.get_bin_path.return_value = None
    device = 'eth0'

    data = linux_network.get_ethtool_data(device)

    assert data == {}

def test_get_ethtool_data_command_failure(linux_network, mock_module):
    device = 'eth0'
    mock_module.run_command.side_effect = [
        (1, '', 'error'),
        (1, '', 'error')
    ]

    data = linux_network.get_ethtool_data(device)

    assert data == {}
