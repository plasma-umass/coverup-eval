# file: lib/ansible/module_utils/facts/network/linux.py:287-316
# asked: {"lines": [287, 289, 290, 292, 293, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316], "branches": [[292, 293], [292, 316], [296, 297], [296, 307], [298, 299], [298, 305], [299, 300], [299, 301], [302, 303], [302, 304], [309, 310], [309, 316], [313, 314], [313, 316]]}
# gained: {"lines": [287, 289, 290, 292, 293, 294, 296, 297, 298, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 316], "branches": [[292, 293], [292, 316], [296, 297], [298, 299], [298, 305], [299, 301], [302, 303], [302, 304], [309, 310], [313, 314], [313, 316]]}

import pytest
import re
from unittest.mock import MagicMock

# Assuming the LinuxNetwork class is defined in ansible/module_utils/facts/network/linux.py
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = "/usr/sbin/ethtool"
    return module

@pytest.fixture
def linux_network(mock_module):
    return LinuxNetwork(module=mock_module)

def test_get_ethtool_data_no_ethtool_path(linux_network, mock_module):
    mock_module.get_bin_path.return_value = None
    result = linux_network.get_ethtool_data("eth0")
    assert result == {}

def test_get_ethtool_data_features(linux_network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "feature1: on\nfeature2: off\n", ""),
        (0, "", "")
    ]
    result = linux_network.get_ethtool_data("eth0")
    assert "features" in result
    assert result["features"] == {"feature1": "on", "feature2": "off"}

def test_get_ethtool_data_timestamping(linux_network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "", ""),
        (0, "SOF_TIMESTAMPING_TX_SOFTWARE\nHWTSTAMP_FILTER_ALL\nPTP Hardware Clock: 2\n", "")
    ]
    result = linux_network.get_ethtool_data("eth0")
    assert "timestamping" in result
    assert result["timestamping"] == ["tx_software"]
    assert "hw_timestamp_filters" in result
    assert result["hw_timestamp_filters"] == ["all"]
    assert "phc_index" in result
    assert result["phc_index"] == 2

def test_get_ethtool_data_no_features(linux_network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "feature1: \nfeature2: off\n", ""),
        (0, "", "")
    ]
    result = linux_network.get_ethtool_data("eth0")
    assert "features" in result
    assert result["features"] == {"feature2": "off"}

def test_get_ethtool_data_no_timestamping(linux_network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "", ""),
        (0, "SOF_TIMESTAMPING_TX_SOFTWARE\n", "")
    ]
    result = linux_network.get_ethtool_data("eth0")
    assert "timestamping" in result
    assert result["timestamping"] == ["tx_software"]
    assert "hw_timestamp_filters" in result
    assert result["hw_timestamp_filters"] == []
    assert "phc_index" not in result
