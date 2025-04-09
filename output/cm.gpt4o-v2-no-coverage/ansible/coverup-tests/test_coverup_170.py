# file: lib/ansible/module_utils/facts/network/hpux.py:61-77
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "branches": [[65, 66], [65, 77], [67, 65], [67, 68], [68, 67], [68, 69]]}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "branches": [[65, 66], [65, 77], [67, 65], [67, 68], [68, 67], [68, 69]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def hpux_network(mock_module):
    return HPUXNetwork(module=mock_module)

def test_get_interfaces_info_no_interfaces(hpux_network, mock_module):
    mock_module.run_command.return_value = (0, "", "")
    result = hpux_network.get_interfaces_info()
    assert result == {}

def test_get_interfaces_info_single_interface(hpux_network, mock_module):
    mock_module.run_command.return_value = (0, "lan0 1500 192.168.1.1 255.255.255.0", "")
    result = hpux_network.get_interfaces_info()
    assert 'lan0' in result
    assert result['lan0']['device'] == 'lan0'
    assert result['lan0']['ipv4']['address'] == '255.255.255.0'
    assert result['lan0']['ipv4']['network'] == '192.168.1.1'
    assert result['lan0']['ipv4']['interface'] == 'lan0'

def test_get_interfaces_info_multiple_interfaces(hpux_network, mock_module):
    mock_module.run_command.return_value = (0, "lan0 1500 192.168.1.1 255.255.255.0\nlan1 1500 10.0.0.1 255.0.0.0", "")
    result = hpux_network.get_interfaces_info()
    assert 'lan0' in result
    assert result['lan0']['device'] == 'lan0'
    assert result['lan0']['ipv4']['address'] == '255.255.255.0'
    assert result['lan0']['ipv4']['network'] == '192.168.1.1'
    assert result['lan0']['ipv4']['interface'] == 'lan0'
    assert 'lan1' in result
    assert result['lan1']['device'] == 'lan1'
    assert result['lan1']['ipv4']['address'] == '255.0.0.0'
    assert result['lan1']['ipv4']['network'] == '10.0.0.1'
    assert result['lan1']['ipv4']['interface'] == 'lan1'
