# file: lib/ansible/module_utils/facts/network/linux.py:287-316
# asked: {"lines": [300, 303], "branches": [[299, 300], [302, 303], [313, 316]]}
# gained: {"lines": [300], "branches": [[299, 300], [313, 316]]}

import pytest
import re
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.linux import LinuxNetwork
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module():
    module = MagicMock(spec=AnsibleModule)
    return module

@pytest.fixture
def linux_network(mock_module):
    return LinuxNetwork(module=mock_module)

def test_get_ethtool_data_no_ethtool_path(linux_network):
    linux_network.module.get_bin_path.return_value = None
    result = linux_network.get_ethtool_data('eth0')
    assert result == {}

def test_get_ethtool_data_ethtool_path_no_features(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.return_value = (1, '', '')
    result = linux_network.get_ethtool_data('eth0')
    assert result == {}

def test_get_ethtool_data_ethtool_path_with_features(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, 'feature1: on\nfeature2: off\n', ''),
        (0, 'SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 2\n', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert result == {
        'features': {
            'feature1': 'on',
            'feature2': 'off'
        },
        'timestamping': ['tx_software'],
        'hw_timestamp_filters': ['none'],
        'phc_index': 2
    }

def test_get_ethtool_data_ethtool_path_with_partial_features(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, 'feature1: on\nfeature2:\n', ''),
        (0, 'SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_NONE\n', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert result == {
        'features': {
            'feature1': 'on'
        },
        'timestamping': ['tx_software'],
        'hw_timestamp_filters': ['none']
    }

def test_get_ethtool_data_ethtool_path_no_timestamping(linux_network):
    linux_network.module.get_bin_path.return_value = '/sbin/ethtool'
    linux_network.module.run_command.side_effect = [
        (0, 'feature1: on\nfeature2: off\n', ''),
        (1, '', '')
    ]
    result = linux_network.get_ethtool_data('eth0')
    assert result == {
        'features': {
            'feature1': 'on',
            'feature2': 'off'
        }
    }
