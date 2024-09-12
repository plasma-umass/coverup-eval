# file: lib/ansible/module_utils/facts/network/linux.py:287-316
# asked: {"lines": [300], "branches": [[296, 307], [299, 300], [309, 316]]}
# gained: {"lines": [300], "branches": [[296, 307], [299, 300]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network():
    module = MagicMock()
    return LinuxNetwork(module=module)

def test_get_ethtool_data_no_ethtool_path(linux_network):
    linux_network.module.get_bin_path.return_value = None
    result = linux_network.get_ethtool_data('eth0')
    assert result == {}

def test_get_ethtool_data_features(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, 'feature1: on\nfeature2: off\n', ''),
        (0, '', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert 'features' in result
    assert result['features'] == {'feature1': 'on', 'feature2': 'off'}

def test_get_ethtool_data_timestamping(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (1, '', ''),  # First command fails
        (0, 'SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 1\n', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert 'timestamping' in result
    assert result['timestamping'] == ['tx_software']
    assert 'hw_timestamp_filters' in result
    assert result['hw_timestamp_filters'] == ['none']
    assert 'phc_index' in result
    assert result['phc_index'] == 1

def test_get_ethtool_data_no_features(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, 'feature1:\nfeature2: \n', ''),
        (0, '', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert 'features' in result
    assert result['features'] == {}

def test_get_ethtool_data_no_timestamping(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, '', ''),
        (0, '', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert 'timestamping' in result
    assert result['timestamping'] == []
    assert 'hw_timestamp_filters' in result
    assert result['hw_timestamp_filters'] == []
    assert 'phc_index' not in result
