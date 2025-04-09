# file lib/ansible/module_utils/facts/network/linux.py:287-316
# lines [300, 303]
# branches ['292->316', '296->307', '299->300', '302->303', '309->316', '313->316']

import pytest
from unittest.mock import MagicMock

# Assuming LinuxNetwork is part of the module ansible.module_utils.facts.network.linux
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = '/usr/sbin/ethtool'
    return LinuxNetwork(module=mock_module)

def test_get_ethtool_data_full_coverage(linux_network, mocker):
    device = 'eth0'
    # Mock run_command to cover all branches
    linux_network.module.run_command.side_effect = [
        (0, "feature1: on\nfeature2: off\n\n: \n", ""),  # Mock ethtool -k output with empty and colon-ending lines
        (0, "SOF_TIMESTAMPING_TX_HARDWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 42\n", ""),  # Mock ethtool -T output
        (1, "", ""),  # Mock ethtool -k failure
        (1, "", "")   # Mock ethtool -T failure
    ]

    # First call to get_ethtool_data to cover successful branches
    data = linux_network.get_ethtool_data(device)

    # Assertions to verify postconditions for successful branches
    assert data['features']['feature1'] == 'on'
    assert data['features']['feature2'] == 'off'
    assert 'timestamping' in data
    assert 'tx_hardware' in data['timestamping']
    assert 'hw_timestamp_filters' in data
    assert 'none' in data['hw_timestamp_filters']
    assert data['phc_index'] == 42

    # Second call to get_ethtool_data to cover failure branches
    data_failure = linux_network.get_ethtool_data(device)

    # Assertions to verify postconditions for failure branches
    assert 'features' not in data_failure
    assert 'timestamping' not in data_failure
    assert 'hw_timestamp_filters' not in data_failure
    assert 'phc_index' not in data_failure

    # Verify that run_command was called with the correct parameters
    linux_network.module.run_command.assert_any_call(['/usr/sbin/ethtool', '-k', device], errors='surrogate_then_replace')
    linux_network.module.run_command.assert_any_call(['/usr/sbin/ethtool', '-T', device], errors='surrogate_then_replace')
