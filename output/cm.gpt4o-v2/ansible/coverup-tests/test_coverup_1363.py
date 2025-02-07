# file: lib/ansible/module_utils/facts/network/hpux.py:48-59
# asked: {"lines": [49, 50, 51, 52, 53, 54, 55, 56, 57, 59], "branches": [[52, 53], [52, 59], [54, 52], [54, 55], [55, 52], [55, 56]]}
# gained: {"lines": [49, 50, 51, 52, 53, 54, 55, 56, 57, 59], "branches": [[52, 53], [52, 59], [54, 55], [55, 52], [55, 56]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def hpux_network(mock_module):
    return HPUXNetwork(module=mock_module)

def test_get_default_interfaces_no_default_route(hpux_network, mock_module):
    mock_module.run_command.return_value = (0, "Destination        Gateway            Flags     Refs     Use  Interface\n", "")
    result = hpux_network.get_default_interfaces()
    assert result == {}

def test_get_default_interfaces_with_default_route(hpux_network, mock_module):
    mock_module.run_command.return_value = (0, "default            192.168.1.1        UG        0        0    0\n", "")
    result = hpux_network.get_default_interfaces()
    assert result == {
        'default_interface': '0',
        'default_gateway': '192.168.1.1'
    }
