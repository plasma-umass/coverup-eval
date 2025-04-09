# file: lib/ansible/module_utils/facts/network/linux.py:287-316
# asked: {"lines": [287, 289, 290, 292, 293, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316], "branches": [[292, 293], [292, 316], [296, 297], [296, 307], [298, 299], [298, 305], [299, 300], [299, 301], [302, 303], [302, 304], [309, 310], [309, 316], [313, 314], [313, 316]]}
# gained: {"lines": [287, 289, 290, 292, 293, 294, 296, 297, 298, 299, 301, 302, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316], "branches": [[292, 293], [292, 316], [296, 297], [296, 307], [298, 299], [298, 305], [299, 301], [302, 304], [309, 310], [309, 316], [313, 314]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network():
    module = MagicMock()
    return LinuxNetwork(module)

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
