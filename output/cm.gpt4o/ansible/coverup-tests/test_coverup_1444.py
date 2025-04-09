# file lib/ansible/module_utils/facts/network/linux.py:287-316
# lines [300, 303]
# branches ['299->300', '302->303', '313->316']

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_module(mocker):
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/sbin/ethtool')
    module.run_command = Mock()
    return module

@pytest.fixture
def linux_network(mock_module):
    from ansible.module_utils.facts.network.linux import LinuxNetwork
    network = LinuxNetwork(module=mock_module)
    return network

def test_get_ethtool_data_no_ethtool_path(mocker, linux_network):
    linux_network.module.get_bin_path = Mock(return_value=None)
    data = linux_network.get_ethtool_data('eth0')
    assert data == {}

def test_get_ethtool_data_no_value(mocker, linux_network):
    linux_network.module.run_command = Mock(return_value=(0, "feature1: on\nfeature2:\nfeature3: off", ""))
    data = linux_network.get_ethtool_data('eth0')
    assert 'features' in data
    assert 'feature1' in data['features']
    assert 'feature2' not in data['features']
    assert 'feature3' in data['features']

def test_get_ethtool_data_phc_index(mocker, linux_network):
    linux_network.module.run_command = Mock(side_effect=[
        (0, "feature1: on\nfeature2: off", ""),
        (0, "SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 2", "")
    ])
    data = linux_network.get_ethtool_data('eth0')
    assert 'phc_index' in data
    assert data['phc_index'] == 2
